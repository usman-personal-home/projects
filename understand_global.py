myglobal = 10


def change_global():
    global myglobal
    myglobal = 15

if __name__ == '__main__':
    print("The number is {}".format(myglobal))
    change_global()
    print("The number is {}".format(myglobal))
