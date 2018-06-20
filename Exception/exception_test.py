import sys


def read_file(fp):
    try:
        with open(fp, 'r') as file:
            lines = file.readlines()

        for line in lines:
            print(line.strip())

    except Exception as  e:
        e.message("Hello")
        print("File cannot be opened")


if __name__ == "__main__":
    fp = sys.argv[1]
    print(fp)
    read_file(fp)