class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, i, j = len(s), 0, 0
        charSet, maxLen = set(), 0
        while j < n:
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            maxLen = max(maxLen, j-i+1)
            j += 1
        return maxLen
