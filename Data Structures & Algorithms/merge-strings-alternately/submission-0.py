class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        ind1 = ind2 = 0
        res, switch = "", False
        while ind1 < m or ind2 < n:
            if ind1 < m and not switch:
                res += word1[ind1]
                ind1 += 1
                switch = not switch
            elif ind2 < n and switch:
                res += word2[ind2]
                ind2 += 1
                switch = not switch
            elif ind1 >= n:
                res += word1[ind1]
                ind1 += 1
            elif ind2 >= m:
                res += word2[ind2]
                ind2 += 1
        return res