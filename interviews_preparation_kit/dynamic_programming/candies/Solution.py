# Complete the candies function below.
def cal(ind, arr, ratings):
    if ratings[ind] != -1:
        return ratings[ind]

    # edge case, local min
    if ind == 0 and arr[ind] <= arr[ind+1]:
        ratings[ind] = 1
        return 1
    elif ind == 0:
        ratings[ind] = cal(ind+1, arr, ratings) + 1
        return ratings[ind]


    # edge case, local min
    if ind == len(arr)-1 and arr[ind] <= arr[ind-1]:
        ratings[ind] = 1
        return 1
    elif ind == len(arr)-1:
        ratings[ind] = cal(ind - 1, arr, ratings) + 1
        return ratings[ind]

    # local max
    elif arr[ind-1] < arr[ind] > arr[ind+1]:
        ratings[ind] = max(cal(ind-1, arr, ratings), cal(ind+1, arr, ratings)) + 1
        return ratings[ind]
    # between
    elif arr[ind-1] < arr[ind]:
        left = cal(ind-1, arr, ratings) + 1
        ratings[ind] = left + 1
    elif arr[ind] > arr[ind+1]:
        right = cal(ind+1, arr, ratings)
        ratings[ind] = right + 1
    #     local min
    else:
        ratings[ind] = 1

    return ratings[ind]


def candies(n, arr):
    if arr[0] > arr[1]:
        arr.reverse()
    ratings = [-1] * len(arr)
    for ind in range(0, len(arr)):
        cal(ind, arr, ratings)

    return sum(ratings)


if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline())

    arr = []

    for _ in range(n):
        arr_item = int(f.readline())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
