"""

"""

import argparse
import time

sample_dataset = ''

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', required=False)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    START = time.time()
    args = get_args()

    if args.input_file:
        pass

    else:
        pass

print('\nFinished in {} seconds\n'.format(time.time() - START))
