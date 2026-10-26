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
        dp = [-1]*n # longest subset starting at `idx` including `nums[idx]`

        ## result or answer of this problem, a list, will never have elements more than 32 bcoz we can only do double,
        ## triple, quadruple, etc. and it'll not go beyond 32 times since that's the max we can store (around 4B) and
        ## "1 <= nums[i] <= 2,000,000,000" anyway

        def memoization(idx):
            # Base Case
            if idx == n:
                return []

            if dp[idx] != -1:
                return dp[idx]

            # Explore all cases
            res = [nums[idx]] # We'll always start finding the subset starting from element at idx
            for i in range(idx+1, n):
                if nums[i] % nums[idx] == 0:
                    # find longest sequence starting from `i`
                    temp = [nums[idx]] + memoization(i) # merge the current element with remaining. max it'll take O(32)
                    if len(temp) > len(res):
                        res = temp

            dp[idx] = res
            return res

        # We can choose to include the first element or not, so run the memoization for all the elements
        res = []
        for i in range(n):
            temp = memoization(i)
            if len(temp) > len(res): res = temp
        
        return res
