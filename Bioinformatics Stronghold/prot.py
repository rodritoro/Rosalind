"""
Translating RNA into Protein

Problem
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output
MAMAPRTEINSTRING
"""

import argparse, json

sample_dataset = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

with open('codon_table.json') as f:
    codon_table = json.load(f)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

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

def translate(mrna):
    peptide = ''
    start = get_start_position(mrna)
    stop = get_stop_position(mrna, start)
    for i in range(start, stop, 3):
        codon = mrna[i:i + 3]
        peptide += codon_table[codon]

    return peptide

if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            mrna = f.read()
    else:
        mrna = sample_dataset

print(translate(mrna))
