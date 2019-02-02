"""
Problem
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

Sample Dataset
100 200
Sample Output
7500
"""

import argparse

sample_dataset = '100 200'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def add_odd_ints(start, end):
    total = 0
    for i in range(start, end):
        if i % 2 != 0:
            total += i
    return total

if __name__ == '__main__':
    args = get_args()
    if args.input_file:
        with open(args.input_file) as f:
            nums = f.read().split()
            for i in range(len(nums)):
                nums[i] = int(nums[i])
    else:
        nums = sample_dataset.split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
    start = nums[0]
    end = nums[1] + 1
    print(add_odd_ints(start, end))
