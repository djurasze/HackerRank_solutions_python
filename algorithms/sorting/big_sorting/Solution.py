#!/bin/python3


# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(unsorted, key=int)


if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline()[:-1])

    unsorted = []

    for _ in range(n):
        unsorted_item = f.readline()[:-1]
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print(result)
