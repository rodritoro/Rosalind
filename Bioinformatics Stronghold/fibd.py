"""
Mortal Fibonacci Rabbits

Problem
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Sample Dataset
6 3
Sample Output
4
"""

import argparse

sample_dataset = "6 3"

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def fibonacci_mortal(n, m):
    seq = [0] * n
    seq[0] = 1
    seq[1] = 1

    for i in range(2, n):
        if i == m or i == m + 1:
            seq[i] = seq[i - 1] + seq[i - 2] - 1
        elif i > m + 1 :
            seq[i] = seq[i - 1] + seq[i - 2] - seq[i - (m + 1)]
        else:
            seq[i] = seq[i - 1] + seq[i - 2]
    return seq[-1]


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            n, m = f.read().split(' ')[:2]
    else:
        n, m = sample_dataset.split(' ')[:2]

n = int(n)
m = int(m)

result = fibonacci_mortal(n, m)
print(result)
