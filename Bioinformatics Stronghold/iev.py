"""
Calculating Expected Offspring

Problem
For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

Sample Dataset
1 0 0 1 0 1
Sample Output
3.5
"""

import argparse

sample_dataset = '1 0 0 1 0 1'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args

def calculate_expected_dominant_offspring(couples):
    dominant_offspring_probability = [
    1.0, # AA-AA
    1.0, # AA-Aa
    1.0, # AA-aa
    0.75, # Aa-Aa
    0.5, # Aa-aa
    0 # aa-aa
    ]

    prob_sum = []

    for i in range(len(couples)):
        prob_sum.append(dominant_offspring_probability[i] * couples[i] * 2)
        
    expected_value = sum(prob_sum)

    return expected_value


if __name__ == '__main__':
    args = get_args()

    if args.input_file:
        with open(args.input_file) as f:
            couples = f.read().split(' ')
    else:
        couples = sample_dataset.split(' ')

couples = [float(item) for item in couples]
result = calculate_expected_dominant_offspring(couples)
print(result)
