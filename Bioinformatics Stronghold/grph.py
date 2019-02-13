"""
Overlap Graphs

Problem
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

import argparse

sample_dataset = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
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

def find_edges(strings, k=3):
    adjacency_list = []

    for id1 in strings:
        s = strings[id1]
        for id2 in strings:
            t = strings[id2]
            if s != t:
                sk = s[-k:]
                tk = t[:k]
                if sk == tk:
                    adjacency_list.append((id1, id2))

    return adjacency_list


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        strings = parse_fasta(args.input_file)
    else:
        strings = parse_fasta(sample_dataset, is_file=False)

adjacency_list = find_edges(strings)

for item in adjacency_list:
    print(item[0], item[1])
