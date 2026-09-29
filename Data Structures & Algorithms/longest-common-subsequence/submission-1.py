class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[-1]*len2 for _ in range(len1)]

        # recursive way of finding all possible subsequence and return the max length of common one
        # return LCS of of strings text1 & text2 upto (i.e. from 0 to indexes) idx1 & idx2 respectively
        def memo(idx1, idx2):
            if dp[idx1][idx2] != -1:
                return dp[idx1][idx2]

            # Base case
            if idx1 < 0 or idx2 < 0: # end of either string (while traversing from right to left)
                return 0 # can't be anything common after traversing of both or one text is ended

            # When characters matches update the required length (increment by 1 since found one 
            # matching character) then go to left (decrement indexes) for checking other remaining
            # characters
            if text1[idx1] == text2[idx2]:
                dp[idx1][idx2] = 1 + memo(idx1-1, idx2-1)
                return dp[idx1][idx2]

            # When character don't match explore both the cases possible i.e decrement idx1 once then
            # idx2 once to not miss out on any character being a part of LCS and return the maximum
            # of two cases
            dp[idx1][idx2] = 0 + max(memo(idx1-1, idx2), memo(idx1, idx2-1))
            return dp[idx1][idx2]

        return memo(len1-1, len2-1)

            