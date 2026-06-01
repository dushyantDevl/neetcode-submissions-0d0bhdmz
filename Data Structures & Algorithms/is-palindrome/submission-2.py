class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPalindromeRecursive(l, r):
            if l >= r:
                return True
            
            while l<r and not self.isAlphaNum(s[l]): l += 1
            while l<r and not self.isAlphaNum(s[r]): r -= 1

            if s[l].lower() != s[r].lower(): 
                return False
            
            return isPalindromeRecursive(l+1, r-1)
        
        return isPalindromeRecursive(0, len(s)-1)

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))