import os
from os.path import basename
import pprint
import random


def main():
    mylist = [1, 1, 1, 6, 2, 3, 4, 4, 4, 4]

    # new_list = remove_duplicates_sorted(mylist)
    new_list = find_duplicate_dict(mylist)
    print (new_list)


def find_duplicate_dict(lst):

    duplicate_lst = []
    dup_dict = {}
    for i in lst:
        if dup_dict.has_key(i):
            dup_dict[i] += 1

        else:
            dup_dict[i] = 0

    for k in dup_dict.keys():
        if dup_dict[k] > 0:
            duplicate_lst.append(k)

    return duplicate_lst


if __name__ == '__main__':
    main()


