class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[-1]*(len2+1) for _ in range(len1+1)]

        def shiftIdxMemo(idx1, idx2):
            # Base case (with shifted indexes)
            if idx1 == 0 or idx2 == 0:
                return 0

            # Memoization
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            if text1[idx1-1] == text2[idx2-1]:
                dp[idx1][idx2] = 1 + shiftIdxMemo(idx1-1, idx2-1)
                return dp[idx1][idx2]

            dp[idx1][idx2] = 0 + max(shiftIdxMemo(idx1-1, idx2), shiftIdxMemo(idx1, idx2-1))
            return dp[idx1][idx2]

        return shiftIdxMemo(len1, len2)