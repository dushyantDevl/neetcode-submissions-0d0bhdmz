class Solution:
    def tribonacci(self, n: int) -> int:
        temp = [0, 1, 1]

        if n < 3:
            return temp[n]

        for i in range(3, n+1):
            temp[i % 3] = sum(temp)

        return temp[n % 3]