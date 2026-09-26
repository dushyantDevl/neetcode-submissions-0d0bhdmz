class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # bcoz `-1000 <= target <= 1000` we've total of 2001 values possible, so use the max size list
        dp = [[-1]*(2002) for _ in range(n)]

        def memo(idx, currSum):
            if idx == n:
                return currSum == target

            if dp[idx][currSum] != -1:
                return dp[idx][currSum]

            addCount = memo(idx+1, currSum + nums[idx])
            subtractCount = memo(idx+1, currSum - nums[idx])

            dp[idx][currSum] = addCount + subtractCount

            return dp[idx][currSum]

        return memo(0, 0)