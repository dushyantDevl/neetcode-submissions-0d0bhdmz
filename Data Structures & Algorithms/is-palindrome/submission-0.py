class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_isalnum = ""
        for c in s:
            if c.isalnum(): s_isalnum += c.lower()
        n = len(s_isalnum)
        for i in range(n//2):
            if s_isalnum[i]!=s_isalnum[n-1-i]: return False
        return True