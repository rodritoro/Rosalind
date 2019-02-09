"""
Consensus and Profile

Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

                A T C C A G C T
                G G G C A A C T
                A T G G A T C T
DNA Strings	    A A G C A A C C
                T T G G A A C T
                A T G C C A T T
                A T G G C A C T

            A   5 1 0 0 5 5 0 0
Profile	    C   0 0 1 4 2 0 6 1
            G   1 1 6 3 0 1 0 0
            T   1 5 0 0 0 1 1 6

Consensus	A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

import argparse, sys

sample_dataset = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
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

def build_string_matrix(strings):
    matrix = []
    for id in strings:
        string = strings[id]
        matrix.append(list(string))
    return matrix

def check_equal_string_length(matrix):
    string_length = 0
    for i in range(len(matrix)):
        if i == 0:
            string_length = len(matrix[i])
        else:
            if len(matrix[i]) != string_length:
                sys.exit('DNA strings are not the same length')
    return string_length

def build_profile_dict(string_length):
    profile = {}
    for base in ['A', 'C', 'T', 'G']:
        profile[base] = []
        for i in range(string_length):
            profile[base].append(0)
    return profile

def get_consensus(strings):
    matrix = build_string_matrix(strings)
    string_length = check_equal_string_length(matrix)
    profile = build_profile_dict(string_length)
    consensus = ''

    # Get profiles for each base
    for i in range(len(strings)):
        for j in range(string_length):
            base = matrix[i][j]
            profile[base][j] += 1

    # Calculate consensus
    for i in range(string_length):
        mode = 0
        consensus_base = ''
        for base in profile:
            if profile[base][i] > mode:
                mode = profile[base][i]
                consensus_base = base
        consensus += consensus_base

    return consensus, profile

if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        strings = parse_fasta(args.input_file)
    else:
        strings = parse_fasta(sample_dataset, is_file=False)

consensus, profile = get_consensus(strings)

# Print with the appropriate formatting
print(consensus)
for base in ['A', 'C', 'G', 'T']:
    print(base + ':',  ' '.join([str(p) for p in profile[base]]))
