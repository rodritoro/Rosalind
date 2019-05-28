"""
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string
implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three
reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop
codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids
until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
"""

import argparse
import time

sample_dataset = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


def get_codon_table():
    with open('codon_table.json') as f:
        codon_table = json.loads(f.read())
    return codon_table


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


def get_reverse_strand(forward_strand):
    inverse_forward = forward_strand[::-1]
    reverse_strand = ''
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for base in inverse_forward:
        reverse_strand += complements[base]

    return reverse_strand


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        pass

    else:
        strings = parse_fasta(sample_dataset, is_file=False)
        print(strings)

    for string_id in strings:
        string = strings[string_id]
        complement = get_reverse_strand(string)
        print(string)
        print(complement)


    print('\nFinished in {} seconds\n'.format(time.time() - START))
