class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [-1]*59 # bcoz 2 <= n <= 2

        def memoization(num):
            # Base Case
            ## can't break 1 further since we can only use positive integers (not 0 either)
            if num == 1:
                return 1

            if dp[num] != -1:
                return dp[num]

            # to only break the original value (i.e. `n`) (other steps will break different numbers while 
            ## recursion is going on)
            res = -float('inf')

            for i in range(1, num): # no need to include `num` since we can only break in +ve integers
                ## this will check for every combination of breaking num into +ve integers, for e.g. for n=4
                ## it'll break into (1,3), (2,2), (3,1) then these number can also breaks further e.g 3 into (2,1)
                ## breaking (1,3) to (1,2,1), similarly it'll work for other numbers.
                ## i*(n-i) will be max, or when further break of `n-i` happens while in recursion
                prod = i * max(num-i, memoization(num-i))
                res = max(res, prod)

            dp[num] = res
            return res

        return memoization(n)