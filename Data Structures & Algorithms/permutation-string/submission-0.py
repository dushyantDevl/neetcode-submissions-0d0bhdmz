class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        l, r = 0, n1-1
        s1 = sorted(s1)
        while r < n2:
            if s1 == sorted(s2[l:r+1]):
                return True
            l, r = l+1, r+1
        return False
