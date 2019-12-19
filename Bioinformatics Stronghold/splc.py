"""
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons
to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""

import argparse
import json

sample_dataset = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

sample_output = 'MVYIADKQHVASREAYGHMFKVCA'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()

    return args


def parse_fasta(fasta, is_file=True, return_list=False):
    if is_file == True:
        with open(fasta) as f:
            fasta_lines = f.read().split('\n')
    else:
        fasta_lines = fasta.split('\n')

    strings_dict = {}
    strings_list = []
    for i in range(len(fasta_lines)):
        if fasta_lines[i].startswith('>'):
            new_string_id = fasta_lines[i].replace('>','')
            new_string = ''
            next = i + 1
            while next < len(fasta_lines) and not fasta_lines[next].startswith('>'):
                new_string += fasta_lines[next]
                next += 1
            strings_dict[new_string_id] = new_string
            strings_list.append((new_string_id, new_string))

    if return_list:
        return strings_list
    else:
        return strings_dict


def splice(string, substrings):
    spliced_string = string

    for substring in substrings:
        spliced_string = spliced_string.replace(substring, '')

    return spliced_string


def transcribe(dna_strand):
    return dna_strand.replace('T', 'U')


def get_start_position(mrna):
    for i in range(len(mrna) - 2):
        if mrna[i:i + 3] == 'AUG':
            return i
    print('No start codon found, defaulting to start position 0')
    return 0


def get_stop_position(mrna, start):
    for i in range(start, len(mrna) - 2, 3):
        codon = mrna[i:i + 3]
        if codon_table[codon] == 'Stop':
            return i
    print('No stop codon found, defaulting to end of string minus 2')
    return len(mrna) - 2


def translate(mrna, codon_table, whole_string=False):
    peptide = ''
    if whole_string:
        start = 0
        stop = len(mrna) - 2
    else:
        start = get_start_position(mrna)
        stop = get_stop_position(mrna, start)
    for i in range(start, stop, 3):
        codon = mrna[i:i + 3]
        if codon_table[codon] != "Stop":
            peptide += codon_table[codon]

    return peptide


if __name__ == '__main__':
    args = get_args()

    with open('codon_table.json', 'r') as f:
        codon_table = json.load(f)

    if args.input_file:
        all_strings = parse_fasta(args.input_file, return_list=True)
    else:
        all_strings = parse_fasta(sample_dataset, is_file=False, return_list=True)

    original_string = all_strings[0][1]
    introns = [intron[1] for intron in all_strings[1:]]

    spliced_string = splice(original_string, introns)

    mrna = transcribe(spliced_string)
    peptide = translate(mrna, codon_table, whole_string=True)

    print(peptide)