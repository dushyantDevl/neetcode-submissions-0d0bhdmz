class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = { 0 : 1 }

        def memoization(total):
            if total in dp:
                return dp[total]

            res = 0
            for num in nums:
                if total < num:
                    break
                res += memoization(total - num)
            dp[total] = res
            return res

        return memoization(target)