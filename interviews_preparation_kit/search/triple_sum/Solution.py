

def triplets(a, b, c):
    a = list(sorted(dict.fromkeys(a)))
    b = list(sorted(dict.fromkeys(b)))
    c = list(sorted(dict.fromkeys(c)))

    current_a_ind = 0
    current_c_ind = 0
    result = 0

    for el in b:
        while current_a_ind < len(a) and a[current_a_ind] <= el:
            current_a_ind = current_a_ind + 1
        while current_c_ind < len(c) and c[current_c_ind] <= el:
            current_c_ind = current_c_ind + 1
        result = result + current_a_ind*current_c_ind

    return result

if __name__ == '__main__':
    f = open("data.txt", "r")

    lenaLenbLenc = f.readline().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, f.readline().rstrip().split()))

    arrb = list(map(int, f.readline().rstrip().split()))

    arrc = list(map(int, f.readline().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    print(ans)