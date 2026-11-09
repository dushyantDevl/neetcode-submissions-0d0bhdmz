class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # To apply Partition DP methods, we'll start in reverse order i.e start with the ballon which will 
        # burst at last so that we can keep track of the remaining ballons at each step, to check for all the cases
        # here we can just check for all the cases considering a certain ballon was burst at last

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[-1]*(n+1) for i in range(n+1)]

        def memoization(i, j):
            if i > j:
                return 0 # no coins
            
            if dp[i][j] != -1:
                return dp[i][j]

            res = -float('inf')

            # check for all the ballons in the i -> j partition
            for k in range(i,j+1):
                coins = ((nums[i-1] * nums[k] * nums[j+1]) + # calculate coins for current ballon that's burst
                    # Check for both partitions from i to k-1 and from k+1 to j
                    memoization(i,k-1) + memoization(k+1,j))

                res = max(res, coins)

            dp[i][j] = res
            return res

        return memoization(1,n-2) # exclude `1` which was added later to num (at both end)