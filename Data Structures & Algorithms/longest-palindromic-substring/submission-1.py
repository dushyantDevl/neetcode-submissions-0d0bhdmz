class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Logic: rather than checking for palindrome from corner to middle element
        # do the opposite i.e. go or expand from middle to corner elements

        n, res, resLen = len(s), '', 0

        def palindromeByExpansion(l, r):
            nonlocal resLen, res
            while l >= 0 and r < n and s[l] == s[r]: # expand until it's a palindrome
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1 # expand to left side in s
                r += 1 # expand to right side in s

        for i in range(n):
            # Check for odd length palindrome (middle to corner elements)
            palindromeByExpansion(i, i)

            # Check for even length palindrome (2 middle elements to corner elements)
            palindromeByExpansion(i, i+1)

        return res

