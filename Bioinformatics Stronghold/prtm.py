"""
Problem
In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted
alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the
corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

Sample Dataset
SKADYEK

Sample Output
821.392
"""

import argparse
import time
import numpy as np

sample_dataset = 'SKADYEK'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


def calculate_mass(protein, mass_table):
    total_weight = 0
    for amino_acid in protein:
        total_weight += mass_table[amino_acid]
    rounded_weight = np.round(total_weight, decimals=3)
    return rounded_weight


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    with open('monoisotopic_mass_table.csv') as csv:
        lines = csv.readlines()
        monoisotopic_mass_table = {}
        for line in lines:
            split = line.split(',')
            amino_acid = split[0]
            weight = float(split[1])
            monoisotopic_mass_table[amino_acid] = weight

    if args.input_file:
        pass
    else:
        protein = sample_dataset

    print(calculate_mass(protein, monoisotopic_mass_table))

    print('\nFinished in {} seconds\n'.format(time.time() - START))