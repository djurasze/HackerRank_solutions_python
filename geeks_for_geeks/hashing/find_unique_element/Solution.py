# User function Template for python3
from collections import Counter

class Solution:
    def cal(self, data, k):
        counts = Counter(data)
        return counts.most_common()[-1][0]


if __name__ == '__main__':
    f = open("data.txt", "r")

    ob = Solution()

    n = int(f.readline())
    for i in range(0, n):
        n,k = f.readline().split()
        data = f.readline().split()
        print(ob.cal(data, k))

