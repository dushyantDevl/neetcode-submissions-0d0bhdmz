class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)

        # Tabulation with shifted indexes
        dp = [[-1]*(word2Len+1) for _ in range(word1Len+1)]

        ## Base Case
        for idx_1 in range(word1Len+1): dp[idx_1][0] = idx_1
        for idx_2 in range(word2Len+1): dp[0][idx_2] = idx_2
        
        for idx_1 in range(1, word1Len+1):
            for idx_2 in range(1, word2Len+1):
                if word1[idx_1-1] == word2[idx_2-1]:
                    dp[idx_1][idx_2] = 0 + dp[idx_1-1][idx_2-1]
                else:
                    insertion = 1 + dp[idx_1][idx_2-1]
                    deletion = 1 + dp[idx_1-1][idx_2]
                    replaced = 1 + dp[idx_1-1][idx_2-1]

                    dp[idx_1][idx_2] = min(insertion, deletion, replaced)

        return dp[word1Len][word2Len]