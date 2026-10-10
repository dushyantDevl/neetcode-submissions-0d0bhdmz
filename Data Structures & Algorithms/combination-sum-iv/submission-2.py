class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 0 initialized, so that we can start counting from zero for every 
        # possible total (midway while the loop is running and the value of
        # total can be anything between 0 to target)
        dp = [0] * (target+1) 

        # Base Case
        dp[0] = 1 # only one way to make sum=0, by not selecting any number
        
        for total in range(1, target+1):
            for num in nums:
                dp[total] += dp[total-num]

        return dp[target]