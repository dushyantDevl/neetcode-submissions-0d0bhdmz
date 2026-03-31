class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n, i = len(word1), len(word2), 0
        res = ""
        for i in range(m+n):
            if i < m: res += word1[i]
            if i < n: res += word2[i]
        return res