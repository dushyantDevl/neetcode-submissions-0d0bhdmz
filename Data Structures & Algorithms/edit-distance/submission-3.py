class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)

        # Tabulation with shifted indexes and space optimization
        prev, curr = [0]*(word2Len+1), [0]*(word2Len+1)

        ## Base Case
        for idx_2 in range(word2Len+1): prev[idx_2] = idx_2
        
        for idx_1 in range(1, word1Len+1):
            # to match the `if idx_2 == 0: return idx_1` base case 
            curr[0] = idx_1 
            for idx_2 in range(1, word2Len+1):
                if word1[idx_1-1] == word2[idx_2-1]:
                    curr[idx_2] = 0 + prev[idx_2-1]
                else:
                    curr[idx_2] = 1 + min(curr[idx_2-1], prev[idx_2], prev[idx_2-1])

            prev = curr.copy()

        return prev[word2Len]