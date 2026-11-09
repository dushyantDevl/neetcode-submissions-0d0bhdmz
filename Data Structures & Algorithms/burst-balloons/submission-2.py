class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # To apply Partition DP methods, we'll start in reverse order i.e start with the ballon which will 
        # burst at last so that we can keep track of the remaining ballons at each step, to check for all the cases
        # here we can just check for all the cases considering a certain ballon was burst at last

        nums = [1] + nums + [1]
        n = len(nums)

        # Tabulation (Bottom-Up approach)
        dp = [[0]*(n+1) for _ in range(n+1)] # initializing like this will also take care of i>j base case

        for i in range(n-1,0,-1): # was from 1 to n-1 in  memoization approach
            for j in range(1,n-1,): # was from n-1 to 1 in memoization approach
                if i > j: # without this dp, will end up storing `-float('inf')` as minimum values while it should be 0 
                    continue
                res = -float('inf')
                # check for all the ballons in the i -> j partition
                for k in range(i,j+1):
                    coins = ((nums[i-1] * nums[k] * nums[j+1]) + # calculate coins for current ballon that's burst
                        # Check for both partitions from i to k-1 and from k+1 to j
                        dp[i][k-1] + dp[k+1][j])

                    res = max(res, coins)

                dp[i][j] = res
        
        return dp[1][n-2]