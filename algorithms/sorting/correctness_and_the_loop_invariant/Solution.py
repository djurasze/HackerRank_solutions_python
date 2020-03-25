

def insertion_sort(l):
    # FOR loop invariant: array l[0:1] is sorted
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        # WHILE loop invariant: all elements in l[i:i+1] are greater or equal to key and are sorted
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           # WHILE loop invariant: all elements in l[j+1:i+1] are greater or equal to key and are sorted
        # WHILE loop invariant: all elements in l[j+1:i+1] are greater or equal to key and are sorted
        l[j+1] = key
        # FOR loop invariant: array l[0:i+1] is sorted
    # FOR loop invariant: array l[0:len(l)] is sorted


f = open("data.txt", "r")


m = int(f.readline().strip())
ar = [int(i) for i in f.readline().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))