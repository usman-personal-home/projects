import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 1, 1, 6, 2, 3, 4, 4, 4, 4]

    # new_list = remove_duplicates_sorted(mylist)
    new_list = find_unique(mylist)
    print (new_list)


def find_unique(lst):

    unique_lst = []

    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

if __name__ == '__main__':
    main()


