class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]

        # Tabulation (Bottom-Up)

        # Base Case
        ## to avoid the negative indexes errors, shift the indexes by 1 to right to match the base case
        ## of Top-Down approach for e.g idx1=1 actually means we're checking on index=2 in text1, 
        ## similarly we'll write base case for idx1 or idx2 equals to 0 (since the shifting is done
        ## for both indexes) instead of checking idx1 < 0 or idx2 < 0 like we did in Top-Down approach
        ## although there also we can do the same shifting, that will work the same way and we can 
        ## directly copy that to write the Bottom-Up 
        for idx1 in range(len1+1): dp[idx1][0] = 0
        for idx2 in range(len2+1): dp[0][idx2] = 0

        for idx1 in range(1, len1+1):
            for idx2 in range(1, len2+1):
                if text1[idx1-1] == text2[idx2-1]:
                    dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
                else:
                    dp[idx1][idx2] = 0 + max(dp[idx1-1][idx2], dp[idx1][idx2-1])

        return dp[len1][len2]