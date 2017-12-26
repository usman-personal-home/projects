import os
import pprint


def digitsum(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    return sum

if __name__ == '__main__':
    print(digitsum(15))

