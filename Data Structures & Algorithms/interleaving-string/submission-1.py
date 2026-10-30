class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len, s2Len, s3Len = len(s1), len(s2), len(s3)
        if s1Len + s2Len != s3Len:
            return False    
        
        # Tabulation (Bottom-Up)
        dp = [[False]*(s2Len+1) for _ in range(s1Len+1)]
        
        ## Base Case
        dp[s1Len][s2Len] = True

        for i1 in reversed(range(s1Len+1)):
            for i2 in reversed(range(s2Len+1)):
                if i1 < s1Len and s1[i1] == s3[i1+i2] and dp[i1+1][i2]:
                    dp[i1][i2] = True
                if i2 < s2Len and s2[i2] == s3[i1+i2] and dp[i1][i2+1]:
                    dp[i1][i2] = True

        return dp[0][0]