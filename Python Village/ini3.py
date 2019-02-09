"""
Strings and Lists

Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102
Sample Output
Humpty Dumpty
"""

import argparse

sample_string = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
sample_list = [22, 27, 97, 102]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()
    return args

def get_string_and_list(file):
    with open(file) as f:
        input = f.read()
        input = input.split()
    string = input[0]
    list = input[1:]
    for i in range(len(list)):
        list[i] = int(list[i])
    return string, list

def strings_and_lists(string, list):
    start1 = list[0]
    end1 = list[1] + 1
    start2 = list[2]
    end2 = list[3] + 1
    cut1 = string[start1:end1]
    cut2 = string[start2:end2]
    return ' '.join([cut1, cut2])


if __name__ == '__main__':
    args = get_args()
    string, list = get_string_and_list(args.input_file)
    print(strings_and_lists(string, list))
