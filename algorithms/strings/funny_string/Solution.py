def funnyString(s):
    s_ascii = [ord(el) for el in s]
    s_ascii_neighbours_abs_diffs = [abs(s_ascii[i]-s_ascii[i+1]) for i in range(len(s_ascii)-1)]
    result =  s_ascii_neighbours_abs_diffs == list(reversed(s_ascii_neighbours_abs_diffs))
    return "Funny" if result else "Not Funny"

if __name__ == '__main__':
    f = open("data.txt", "r")

    q = int(f.readline().strip())

    for q_itr in range(q):
        s = f.readline().strip()

        result = funnyString(s)

        print(result)

