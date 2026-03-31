class Solution:
    def isPalindrome(self, s:str) -> bool:
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]: return False
        return True

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s): return True
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if self.isPalindrome(temp): return True
            
        return False
