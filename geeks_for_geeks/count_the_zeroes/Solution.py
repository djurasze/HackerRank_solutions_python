# User function Template for python3
import math

class Solution:
    def countZeroes(self, arr, n):
        return n - self.findJunction(arr, 0, n - 1)
        # code here

    def findJunction(self, arr, start, end):
        # no result
        if start == end and arr[start] == 1:
            return end + 1
        if start == end:
            return start
        if start + 1 == end and arr[start] == 0:
            return start
        if start + 1 == end and arr[end] == 0:
            return end
        if start + 1 == end and arr[end] == 1:
            return end + 1
        mid = math.floor(start + ((end - start)/2))
        if arr[mid] == 1:
            return self.findJunction(arr, mid, end)
        else:
            return self.findJunction(arr, start, mid)


if __name__ == '__main__':
    f = open("data.txt", "r")

    data = list(map(int, f.readline().strip().split()))
    ob = Solution()
    print(ob.countZeroes(data, len(data)))