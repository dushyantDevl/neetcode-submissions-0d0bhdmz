class Solution:
    def isPalindrome(self, s:str) -> bool:
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]: return False
        return True

    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s): return True
        l, r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return self.isPalindrome(s[l+1:r+1]) or self.isPalindrome(s[l:r])
            l, r = l+1, r-1
        return True