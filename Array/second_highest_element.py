if __name__ == '__main__':
    arr = [6, 6, 6, 5]
    high = 0
    second = 0

    for i in arr:
        if i > high:
            second = high
            high = i
        elif second < i < high:
            second = i
    print second
