"""
Finding a Shared Motif

Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC
"""

import argparse
import time
import random

sample_dataset = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

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

def get_longest_common_substrings(strings):
    common_motifs = set()
    ids = [id for id in strings]

    strlength = 0
    chosen_id = ''
    for id in ids:
        string = strings[id]
        if strlength == 0:
            strlength = len(string)
            chosen_id = id
        else:
            if len(string) < strlength:
                strlength = len(string)
                chosen_id = id

    string = strings[chosen_id]
    print('Shortest string length: {}'.format(len(string)))
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            motif = string[i:j]
            if not motif in common_motifs and len(motif) > 1:
                common_motifs.add(motif)
    ids.remove(id)

    while len(ids) != 0:
        motifs_to_remove = []
        id = random.choice(ids)
        string = strings[id]
        for motif in common_motifs:
            if not motif in string:
                motifs_to_remove.append(motif)
        for motif in motifs_to_remove:
            common_motifs.remove(motif)
        ids.remove(id)

    longest = 0
    for motif in common_motifs:
        if len(motif) > longest:
            longest = len(motif)

    common_motifs = [motif for motif in common_motifs if len(motif) == longest]

    return common_motifs


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        strings = parse_fasta(args.input_file)

    else:
        strings = parse_fasta(sample_dataset, is_file=False)

result = get_longest_common_substrings(strings)
print(result)
print()
print(result[-1])

print('\nFinished in {} seconds\n'.format(time.time() - START))
