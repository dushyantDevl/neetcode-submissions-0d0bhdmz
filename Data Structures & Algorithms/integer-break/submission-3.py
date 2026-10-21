class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*59
        
        # Tabulation (Bottom-Up)
        dp[1] = 1 # Base Case

        for num in range(2, n+1):
            res = 0 if num == n else num # to only break the original value (i.e. `n`)
            for i in range(1, num): # no need to include `num` since we can only break in +ve integers
                ## this will check for every combination of breaking num into +ve integers, for e.g. for n=4
                ## it'll break into (1,3), (2,2), (3,1) then these number can also breaks further e.g 3 into (2,1)
                ## breaking (1,3) to (1,2,1), similarly it'll work for other numbers
                res = max(res, dp[i] * dp[num-i])

            dp[num] = res

        return dp[n]