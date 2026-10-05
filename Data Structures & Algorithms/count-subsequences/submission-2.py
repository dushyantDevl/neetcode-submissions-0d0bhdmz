class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)
        # Tabulation (Bottom-Up)
        ## shift index by 1 (to right), to write the similar solution as Memoization
        dp = [[0]*(tLen+1) for _ in range(sLen+1)]

        # Base Case
        for idx_s in range(sLen+1):
            dp[idx_s-1][0] = 1 # whole `t` is traversed, so always atleast 1 occurence will be counted
        # for idx_t in range(1, tLen+1): # start from 1 to not overwrite what above loop filled or just remove this loop, since we've initialized the dp list with 0 already
            # dp[0][idx_t-1] = 0 # whole `s` is traversed, without finding any occurence of `t`

        for idx_s in range(1, sLen+1):
            for idx_t in range(1, tLen+1):
                if s[idx_s-1] == t[idx_t-1]: # character's matched!
                    dp[idx_s][idx_t] = (
                        # check if remaining `t` i.e. `t[:idx_t]` is subsequence of the remaining `s`
                        dp[idx_s-1][idx_t-1]
                        + 
                        ## also check for the possibility where we've to match the character at `idx_t` with 
                        ## character at any other index of `s` (both should match tho)
                        dp[idx_s-1][idx_t]
                    )

                else: # character's didn't matched
                    ## just skip the character of `s` (by decrementing `idx_s`) which doesn't match 
                    ## with character at `idx_t` of `t`
                    dp[idx_s][idx_t] = dp[idx_s-1][idx_t]

        return dp[sLen][tLen]
