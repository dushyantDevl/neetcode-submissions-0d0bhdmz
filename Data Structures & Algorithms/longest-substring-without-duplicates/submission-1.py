class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, i, maxLen = len(s), 0, 0
        if n == 0 or n == 1: return n
        hashSet = set()
        for j in range(n):
            if s[j] in hashSet:
                maxLen = max(maxLen, j-i)
                i = j
            hashSet.add(s[j])
        return maxLen

