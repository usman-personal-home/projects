"""
read raw input

"""

import sys


def read_file(fp):
    with open(fp, 'r') as file:
        lines = file.readlines()

    for line in lines:
        print(line.strip())


def read_file2(fp):
    with open(fp, 'r') as file:

        for line in file:
            print(line.strip())


if __name__ == "__main__":
    fp = sys.argv[1]
    print(fp)
    read_file2(fp)