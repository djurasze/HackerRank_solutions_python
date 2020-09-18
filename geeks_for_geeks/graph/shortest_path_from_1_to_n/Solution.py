# User function Template for python3

class Solution:
    def minStep(self, n):
        return self.minStepRec(1, n)

    def minStepRec(self, n, current):
        if (current == n):
            return 0

        if (current % 3 == 0):
            return 1 + self.minStepRec(n, current // 3)
        else:
            return n + self.minStepRec(n, current-1)


if __name__ == '__main__':
    f = open("data.txt", "r")

    n = int(f.readline())
    ob = Solution()
    print(ob.minStep(n))