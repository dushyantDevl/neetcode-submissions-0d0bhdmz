class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        
        # if total sum is odd we can't divide in two equal halve subset (with equal sum)
        if total % 2 != 0:
            return False
        
        ## If there exist a subset whose sum is total/2, then other subset will automatically have sum 
        ## equal to total/2
        target = total//2

        # Tabulation (Bottom-Up, opposite traversal of recursion method)
        dp = [[False]*(target+1) for _ in range(n)]

        # Base cases
        for i in range(n): dp[i][0] = True # if we get the target sum
        if target >= nums[0]: dp[0][nums[0]] = True # Only possible when at index=0, the element itself equal to target

        for idx in range(1, n):
            for t in range(1, target+1):
                take = dp[idx-1][t - nums[idx]] if t >= nums[idx] else False
                notTake = dp[idx-1][t] # ignore the element at current index
            
                dp[idx][t] = take or notTake

        return dp[n-1][target]