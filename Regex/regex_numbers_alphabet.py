import re
import sys


if __name__ == "__main__":
    strs = ["abc cdedede 1234.345 3456.444 adbcd12  asdf 1234"]

    #re1 = re.compile(r"\d+\.\d+") #1234.345
    #re1 = re.compile(r"([a-z0-9]+)")
    re1 = re.compile(r"\b\w{3}\b")

    for line in strs:
        match = re1.findall(line)
        if match:
            print(match)
