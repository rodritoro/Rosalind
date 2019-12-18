"""
Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse
palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may
return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

import argparse

sample_dataset = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()

    return args


def parse_fasta(fasta, is_file=True):
    if is_file == True:
        with open(fasta) as f:
            fasta_lines = f.read().split('\n')
    else:
        fasta_lines = fasta.split('\n')

    strings = {}
    for i in range(len(fasta_lines)):
        if fasta_lines[i].startswith('>'):
            new_string_id = fasta_lines[i].replace('>','')
            new_string = ''
            next = i + 1
            while next < len(fasta_lines) and not fasta_lines[next].startswith('>'):
                new_string += fasta_lines[next]
                next += 1
            strings[new_string_id] = new_string

    return strings


def reverse_complement(dna_strand):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_dna_strand = ''

    reversed_dna_strand = dna_strand[::-1]

    for base in reversed_dna_strand:
        complement_dna_strand += complements[base]

    return complement_dna_strand


def is_reverse_palindrome(sequence):
    if sequence == reverse_complement(sequence):
        return True
    else:
        return False


def find_restriction_sites(dna_strand):
    restriction_sites = []
    for i in range(len(dna_strand) - 3):
        for j in range(4, 13):
            if i + j <= len(dna_strand):
                sequence = dna_strand[i:i+j]
                if is_reverse_palindrome(sequence):
                    restriction_sites.append({'position': i + 1, 'length': j, 'sequence': sequence})
    return restriction_sites


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        strings = parse_fasta(args.input_file)
    else:
        strings = parse_fasta(sample_dataset, is_file=False)

    for string in strings:
        restriction_sites = find_restriction_sites(strings[string])
        for site in restriction_sites:
            print(f'{site["position"]} {site["length"]}')