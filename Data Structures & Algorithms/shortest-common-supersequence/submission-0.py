class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ## for shortestCommonSupersequence, take the longestCommonSequence ONCE to form a start forming
        ## the superSequence of min. length and then take the remaining characters from BOTH 
        ## strings (in ORDER)
        len1, len2 = len(str1), len(str2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        
        def longestCommonSubsequence(text1: str, text2: str) -> int:

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


        longestCommonSubsequence(str1, str2)
        ## Now we can find the common subsequence string using the dp list by traversing from 
        ## bottom-right cell, when both characters match move to upper-left neighbor diagonal element
        ## since that's how we fill the dp table of LCS when matching character is found and when
        ## characters don't match move to the max of either upper or left cell (since that's what we
        ## did while filling dp table when characters don't match), in case if both cells has same 
        ## value we can traverse to any one.

        res = ""
        i, j = len1, len2

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]: # "-1" because of index shift method used while finding LCS
                res += str1[i-1]
                i, j = i-1, j-1

            elif dp[i-1][j] > dp[i][j-1]: # upper cell has greater value, traverse to that cell
                ## since we've moved on from the current row, store the corresponding character 
                ## of the current cell (before going above)
                res += str1[i-1]  
                i -= 1

            else: # left cell has greater value, traverse to that cell
                ## since we've moved on from the current column, store the corresponding character 
                ## of the current cell (before going left)
                res += str2[j-1]
                j -= 1

        ## Because above loop, just ends when both strings still has characters, just add those 
        ## remaining one's
        while i > 0:
            res += str1[i-1]  
            i -= 1
        while j > 0:
            res += str2[j-1]
            j -= 1

        return res[::-1]