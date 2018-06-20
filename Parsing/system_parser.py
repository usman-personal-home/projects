if __name__ == '__main__':
    f = open('input.log', 'r')
    lines = f.readlines()
    f.close()
    print(len(lines))

    f3 = open('input.log', 'r')
    data = f3.read()
    f3.close()
    print(len(data))
    with open('input.log', "r") as file:
        #print(file.readlines())
        #for line in file.readlines():
        for line in file:
            print line
            print len(line)
