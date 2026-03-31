class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        s, t = sorted(s), sorted(t)
        for i in range(len(s)):
            if s[i]!=t[i]: return False
        return True