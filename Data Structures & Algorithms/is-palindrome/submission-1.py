class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_isalnum = ""
        for c in s:
            if c.isalnum(): s_isalnum += c.lower()
        return s_isalnum == s_isalnum[::-1]