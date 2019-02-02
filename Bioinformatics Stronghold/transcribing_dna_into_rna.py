"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
"""

import argparse

sample_dataset = 'GATGGAACTTGACTACGTAAATT'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def transcribe(dna_strand):
    rna_strand = dna_strand.replace('T', 'U')

    return rna_strand

if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            dna_strand = f.read()
    else:
        dna_strand = sample_dataset

    print(transcribe(dna_strand))
