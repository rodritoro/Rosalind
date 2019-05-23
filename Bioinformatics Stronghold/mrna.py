"""
Problem
For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
"""

import argparse
import time
import json

sample_dataset = 'MA'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


def get_codon_table():
    with open('codon_table.json') as f:
        codon_table = json.loads(f.read())
    return codon_table


def calculate_possible_permutations(protein_string, codon_table):
    permutations = 1
    for amino_acid in protein_string:
        codons = 0
        for codon in codon_table:
            if codon_table[codon] == amino_acid:
                codons += 1
        permutations *= codons
    permutations *= 3
    return permutations % 1000000


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            protein_string = f.read().strip()
    else:
        protein_string = sample_dataset

    codon_table = get_codon_table()

    answer = calculate_possible_permutations(protein_string, codon_table)
    print(answer)

    print('\nFinished in {} seconds\n'.format(time.time() - START))
