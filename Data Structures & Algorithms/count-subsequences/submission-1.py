class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)

        ## shift index by 1 (to right), to later write the similar solution for tabulation
        dp = [[-1]*(tLen+1) for _ in range(sLen+1)]


        def memoization(idx_s, idx_t):
            # Base Case
            ## `t` is fully traversed, that means we've found out `t` is subsequence of `t`, so count
            ## that occurence as 1
            if idx_t == 0: 
                return 1
            ## `s` is fully traversed without finding the occurence of `t` (if it did it would've 
            ## return 1 bcoz of above base case, so yes! location of both lines in base cases matters)
            if idx_s == 0: 
                return 0

            # Caching
            if dp[idx_s][idx_t] != -1:
                return dp[idx_s][idx_t]

            # Explore all cases
            if s[idx_s-1] == t[idx_t-1]: # character's matched!
                dp[idx_s][idx_t] = (
                    # check if remaining `t` i.e. `t[:idx_t]` is subsequence of the remaining `s`
                    memoization(idx_s-1, idx_t-1)
                    + 
                    ## also check for the possibility where we've to match the character at `idx_t` with 
                    ## character at any other index of `s` (both should match tho)
                    memoization(idx_s-1, idx_t)
                )

                return dp[idx_s][idx_t]

            else: # character's didn't matched
                ## just skip the character of `s` (by decrementing `idx_s`) which doesn't match 
                ## with character at `idx_t` of `t`
                dp[idx_s][idx_t] = memoization(idx_s-1, idx_t)
                return dp[idx_s][idx_t]
        
        # dp[sLen-1][tLen-1]
        return memoization(sLen,tLen)
