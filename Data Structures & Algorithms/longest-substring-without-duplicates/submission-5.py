class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, l, maxLen = len(s), 0, 0
        charSet = set()
        for r in range(n):
            if s[r] in charSet: # Keep shrinking the window until duplicate is found
                charSet.remove(s[l])
                l = r
            charSet.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen