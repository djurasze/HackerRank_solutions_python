#!/bin/python3

import os


# Complete the runningTime function below.
def runningTime(arr):
    moves = 0
    for i in range(len(arr)):
        j = i-1
        current = arr[i]
        while j >= 0 and current < arr[j]:
            arr[j+1] = arr[j]
            moves += 1
            j -= 1
        arr[j+1] = current

    return moves


if __name__ == '__main__':
    f = open("data.txt", "r")


    n = int(f.readline().strip())

    arr = list(map(int, f.readline().strip().split()))

    result = runningTime(arr)

    print(result)
