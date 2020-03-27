#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the almostSorted function below.
def swap(copy, first, second):
    copy[first], copy[second] = copy[second], copy[first]


def check_if_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
    # return all(l[i] <= l[i+1] for i in range(len(l)-1))


def try_sort_by_swap(arr):
    prev = arr[0]
    first = None
    second = None
    for index in range(1,len(arr)):
        if prev > arr[index] and first is None:
            first = index - 1
            second = index
        elif second is not None and arr[index] < arr[second]:
            second = index
        prev = arr[index]
    copy = arr.copy()
    swap(copy, first, second)
    result = check_if_sorted(copy)
    return (True, 'yes\nswap {} {}'.format(first+1, second+1)) if result is True else (False, "no")


def try_sort_by_reverse(arr):
    prev = arr[0]
    start = None
    end = None
    for index in range(1, len(arr)):
        if prev > arr[index] and start is None:
            start = index - 1
        elif start is not None and prev >= arr[index]:
            end = index - 1
        elif start is not None and prev < arr[index]:
            end = index -1
            break
        prev = arr[index]
    if end is None and index == len(arr)-1:
        end = len(arr)-1
    reversed_sub = list(reversed(arr[start:end+1]))
    result = check_if_sorted(arr[:start] + reversed_sub + arr[end+1:])
    return (True, 'yes\nreverse {} {}'.format(start+1, end+1)) if result is True else (False, "no")


def almostSorted(arr):
    if check_if_sorted(arr):
        return 'yes'
    result = try_sort_by_swap(arr)
    return result[1] if result[0] else try_sort_by_reverse(arr)[1]


if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline().strip())

    arr = list(map(int, f.readline().strip().split()))

    result = almostSorted(arr)
    print(result)
