class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n!= 0 else 0
        
        last, last2nd, last3rd = 1, 1, 0

        for _ in range(3, n+1):
            curr = last + last2nd + last3rd
            last3rd = last2nd
            last2nd = last
            last = curr

        return last