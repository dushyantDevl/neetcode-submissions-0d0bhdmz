class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)
        # Tabulation (Bottom-Up) -> Space Optimized
        dp = [0]*(tLen+1)

        # Base Case
        dp[0] = 1

        for idx_s in range(1, sLen+1):
            # since we need the previous element (tLen-1) start from end instead
            for idx_t in range(tLen, 0, -1):
                if s[idx_s-1] == t[idx_t-1]: # character's matched!
                    dp[idx_t] =dp[idx_t-1] + dp[idx_t]

                # else:
                    # dp[idx_t] = dp[idx_t] # redundant! so just remove the `else` condition

        return dp[tLen]