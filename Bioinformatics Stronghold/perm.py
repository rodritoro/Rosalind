"""
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

import argparse
import time

sample_dataset = '3'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


def calculate_permutations(n):
    permutations = []
    counter = 1
    while counter <= n:
        if len(permutations) < 1:
            for i in range(1, n + 1):
                permutations.append(str(i))
        else:
            new_permutations = []
            for permutation in permutations:
                for i in range(1, n + 1):
                    new_permutations.append(permutation + str(i))
            permutations = new_permutations
        counter += 1

    final_permutations = []
    for permutation in permutations:
        no_repeats = True
        for n in permutation:
            amount = permutation.count(n)
            if amount > 1:
                no_repeats = False
        if no_repeats:
            final_permutations.append(permutation)

    return final_permutations


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            n = int(f.read().strip())
    else:
        n = int(sample_dataset)

    permutations = calculate_permutations(n)
    print(len(permutations))
    for permutation in permutations:
        print(' '.join(permutation))

    print('\nFinished in {} seconds\n'.format(time.time() - START))
