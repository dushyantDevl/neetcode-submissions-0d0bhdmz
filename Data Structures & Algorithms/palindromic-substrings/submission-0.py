class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def palindromeByExpansion(l, r):
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]: # expand until it's a palindrome
                res += 1
                # expand from middle element(s) to corner elements
                l, r = l-1, r+1

        for i in range(n):
            # Check for odd length palindrome (middle to corner elements)
            palindromeByExpansion(i, i)

            # Check for even length palindrome (2 middle elements to corner elements)
            palindromeByExpansion(i, i+1)

        return res
