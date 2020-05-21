if __name__ == '__main__':
    f = open("data.txt", "r")

    first_multiple_input = f.readline().strip().split()

    n = int(first_multiple_input[0])

    for i in range(1, n + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        print(sum(map(lambda base: (base if base <= i else i - (base - i)) * 10 ** (2 * i - base - 1), range(1, 2 * i))))


