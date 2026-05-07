class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        i, maxLen = 0, 0
        for j in range(len(s)):
            if s[j] in hashSet:
                maxLen = max(maxLen, j-i)
                i = j
            hashSet.add(s[j])
        return maxLen

