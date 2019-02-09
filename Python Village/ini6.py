"""
Dictionaries

Problem
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

Sample Dataset
We tried list and we tried dicts also we tried Zen

Sample Output
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
"""

import argparse

sample_dataset = 'We tried list and we tried dicts also we tried Zen'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def count_unique_words(string):
    all_words = string.split()
    unique_words = {}
    for word in all_words:
        unique_words[word] = unique_words.get(word, 0) + 1
    return unique_words

if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            string = f.read()
    else:
        string = sample_dataset

    unique_words = count_unique_words(string)

    for word in unique_words:
        print(word, unique_words[word])
