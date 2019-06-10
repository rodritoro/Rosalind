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
import json

sample_dataset = """
"""


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        pass
    else:
        pass

    print('\nFinished in {} seconds\n'.format(time.time() - START))