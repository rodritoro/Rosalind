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
import json

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


def transcribe(dna_string):
    mrna_3_to_5 = ''
    complements = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    for base in dna_string:
        mrna_3_to_5 += complements[base]
    mrna = mrna_3_to_5[::-1]
    return mrna


def translate(mrna_string, codon_table):
    possible_translations = []
    starting_positions = []
    for i in range(0, len(mrna_string) - 2):
        codon = mrna_string[i:i+3]
        if codon == 'AUG':
            starting_positions.append(i)
    for start in starting_positions:
        protein = ''
        for i in range(start, len(mrna_string), 3):
            stop = False
            if i + 3 < len(mrna_string):
                codon = mrna_string[i:i+3]
                aa = codon_table[codon]
                if aa == 'Stop':
                    stop = True
                    break
                else:
                    protein += aa
        if stop:
            possible_translations.append(protein)
    return possible_translations


def get_all_possible_protein_strings(forward_strand):
    codon_table = get_codon_table()
    reverse_strand = get_reverse_strand(forward_strand)
    forward_mrna = transcribe(forward_strand)
    reverse_mrna = transcribe(reverse_strand)
    forward_proteins = translate(forward_mrna, codon_table)
    reverse_proteins = translate(reverse_mrna, codon_table)
    possible_proteins = set(forward_proteins + reverse_proteins)
    return possible_proteins


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        strings = parse_fasta(args.input_file)
    else:
        strings = parse_fasta(sample_dataset, is_file=False)

    for string_id in strings:
        forward_strand = strings[string_id]
        output = get_all_possible_protein_strings(forward_strand)
        for o in output:
            print(o)

    print('\nFinished in {} seconds\n'.format(time.time() - START))
