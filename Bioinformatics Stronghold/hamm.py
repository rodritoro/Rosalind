"""
Computing Point Mutations

Problem

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
Sample Output
7
"""

import argparse

sample_dataset = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def calculate_hamming_distance(s, t):
    if len(s) != len(t):
        return 'Cannot calculate Hamming distance: string length is not equal'

    hamming_distance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamming_distance += 1

    return hamming_distance


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            s, t = f.read().split('\n')[:2]
    else:
        s, t = sample_dataset.split('\n')[:2]

    print(calculate_hamming_distance(s, t))
