class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Divide them in two subsets such that s1 & s2 are sum of those two respectively then
        # what we've to find is just |s1-s2| = target, this is bcoz it's same as creating 
        # every possibilities using '+' or '-' sign on numbers and adding them to get thier sum,
        # if it's equal to target or not, so this problem is same as "Partitions with given difference"
        return self._countPartitions(nums, target)
    
    def _countPartitions(self, arr, diff):
        # `|S1 - S2| = diff` and `S1 + S2 = total` therefore S2 = (total-diff)/2
        
        totalSum = sum(arr)
        target = (totalSum - diff) // 2 # required sum we've to find according to question
        
        # targetSum should be >= 0 and even to satisfy the give condition
        if totalSum - diff < 0 or (totalSum - diff) % 2:
            return 0
        
        n = len(arr)
        # dp[idx][curr] = number of subsets of arr[0..idx] summing to curr
        dp = [[0] * (target + 1) for _ in range(n)]

        # Base row (idx == 0), mirroring the recursive base case
        for curr in range(target + 1):
            if curr == arr[0] == 0:
                dp[0][curr] = 2          # take the zero, or don't
            elif curr == 0 or arr[0] == curr:
                dp[0][curr] = 1          # empty choice, or take arr[0]
            else:
                dp[0][curr] = 0

        # Fill the rest
        for idx in range(1, n):
            for curr in range(target + 1):
                notTake = dp[idx - 1][curr]
                take = dp[idx - 1][curr - arr[idx]] if curr >= arr[idx] else 0
                dp[idx][curr] = take + notTake

        return dp[n - 1][target]