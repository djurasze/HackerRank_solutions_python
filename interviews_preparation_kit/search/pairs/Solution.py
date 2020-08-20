

def pairs(k, arr):
    arr = sorted(arr)
    result = 0
    arr_set = set()
    for el in arr :
        arr_set.add(el)
    for el in arr:
        if el + k in arr_set:
            result = result + 1
    return result



f = open("data.txt", "r")

nk = f.readline().split()

n = int(nk[0])

k = int(nk[1])

arr = list(map(int, f.readline().rstrip().split()))

result = pairs(k, arr)

print(result)