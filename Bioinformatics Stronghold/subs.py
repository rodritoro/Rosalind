"""
Finding a Motif in DNA

Problem
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
"""

import argparse

sample_dataset = """GATATATGCATATACTT
ATAT
"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def get_motif_positions(motif, strand):
    positions = []
    if len(motif) < len(strand):
        for i in range(len(strand) - (len(motif) - 1)):
            if strand[i:i + len(motif)] == motif:
                positions.append(i + 1)
    else:
        print('Motif is longer than DNA strand')
        return []
    return positions

if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            strand, motif = f.read().split('\n')[:2]
    else:
        strand, motif = sample_dataset.split('\n')[:2]

pos = get_motif_positions(motif, strand)

for i in range(len(pos)):
    pos[i] = str(pos[i])

print(' '.join(pos))
