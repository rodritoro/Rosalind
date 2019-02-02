"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT
"""

import argparse

sample_dataset = 'AAAACCCGGT'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def complement(dna_strand):
    complements = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement_dna_strand = ''

    reversed_dna_strand = dna_strand[::-1]

    for base in reversed_dna_strand:
        complement_dna_strand += complements[base]

    return complement_dna_strand


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            dna_strand = f.read().strip()
    else:
        dna_strand = sample_dataset

    print(complement(dna_strand))
