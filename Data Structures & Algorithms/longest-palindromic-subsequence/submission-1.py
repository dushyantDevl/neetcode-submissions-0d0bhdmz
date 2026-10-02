class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Logic:
        ## Find the longest common subequence with given string in reverse order and og order,
        ## here common string just means it's a palindrome (all characters are same from both sides)
        ## so we just have to find the longest one among them

        def longestCommonSubsequence(text1: str, text2: str) -> int:
            len1, len2 = len(text1), len(text2)
            prev = [0]*(len2+1)

            # Tabulation (Bottom-Up) -> Space Optimization 

            # Base Case
            for idx2 in range(len2+1): prev[idx2] = 0

            for idx1 in range(1, len1+1):
                curr = [0]*(len2+1)
                for idx2 in range(1, len2+1):
                    if text1[idx1-1] == text2[idx2-1]:
                        curr[idx2] = 1 + prev[idx2-1]
                    else:
                        curr[idx2] = 0 + max(prev[idx2], curr[idx2-1])
                
                prev = curr

            return prev[len2]

        return longestCommonSubsequence(s, s[::-1])