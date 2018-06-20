import csv
import sys
import pprint

def read_csv_file(fp):
    #print(fp)
    lines = []
    with open(fp, 'rb') as file:
        reader = csv.reader(file)
        #for row in reader:
        for i, row in enumerate(reader):
            #print(type(row))
            #print(row)
            lines.append(row)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            print("{} : {},{} ".format(lines[i][j], i, j ))
    #pprint.pprint(lines)
    #pprint.pprint(lines[0][1])

if __name__ == '__main__':
    read_csv_file(sys.argv[1])