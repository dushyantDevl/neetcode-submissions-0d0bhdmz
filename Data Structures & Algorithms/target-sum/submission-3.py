class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def memo(idx, currSum):
            if idx == n:
                # return 1 iff we've achieved the target by certain pattern of using numbers with +,-
                # return 0 if some pattern doesn't add ups to target
                return currSum == target

            if (idx,currSum) in dp:
                return dp[(idx,currSum)]

            addCount = memo(idx+1, currSum + nums[idx])
            subtractCount = memo(idx+1, currSum - nums[idx])

            dp[(idx,currSum)] = addCount + subtractCount

            return dp[(idx,currSum)]

        return memo(0, 0)