class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Why Sorting?, Seque, Sequencence
        ## 1. Since we require subset and not subsequence, it'll correct even if the order isn't same as in `nums`.
        ## 2. We just have to check once for the require condition bcoz greater no. will be ahead, so just check the 
        ## remainder of the greater one with its previous element (no need to check for `previous % greater`)
        ## 3. if the later number is divisible by previous number than its divisible by previous of previous too e.g.
        ## [2,4,8] `4 % 2 == 0` then `8 % 2` is also `0`
        nums.sort()
        n = len(nums)
        
        # Tabulation (Bottom-Top)
        dp = [[num] for num in nums] # longest subset starting at `idx` including `nums[idx]`

        ## result or answer of this problem, a list, will never have elements more than 32 bcoz we can only do double,
        ## triple, quadruple, etc. and it'll not go beyond 32 times since that's the max we can store (around 4B) and
        ## "1 <= nums[i] <= 2,000,000,000" anyway

        res = []
        for idx in range(n-1,-1,-1):
            for i in range(idx+1, n):
                if nums[i] % nums[idx] == 0:
                    # find longest sequence starting from `i`
                    temp = [nums[idx]] + dp[i] # merge the current element with remaining. max it'll take O(32)
                    dp[idx] = temp if len(temp) > len(dp[idx]) else dp[idx]

            res = dp[idx] if len(dp[idx]) > len(res) else res
        return res