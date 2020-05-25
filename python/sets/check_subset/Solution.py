def is_subset(first_set, second_set):
    return  first_set.issubset(second_set)


if __name__ == '__main__':
    f = open("data.txt", "r")

    first_multiple_input = f.readline().strip().split()

    n = int(first_multiple_input[0])

    for i in range(1, n + 1):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        f.readline()
        first_set = set(map(int, f.readline().strip().split(' ')))
        f.readline()
        second_set = set(map(int, f.readline().strip().split(' ')))
        print(is_subset(first_set, second_set))


