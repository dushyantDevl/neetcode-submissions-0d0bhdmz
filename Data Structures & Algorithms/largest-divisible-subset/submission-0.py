class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Why Sorting?
        ## 1. Since we require subset and not subsequence, it'll correct even if the order isn't same as in `nums`.
        ## 2. We just have to check once for the require condition bcoz greater no. will be ahead, so just check the 
        ## remainder of the greater one with its previous element (no need to check for `previous % greater`)
        ## 3. if the later number is divisible by previous number than its divisible by previous of previous too e.g.
        ## [2,4,8] `4 % 2 == 0` then `8 % 2` is also `0`
        nums.sort()
        n = len(nums)
        dp = {} # (idx, prevNum): []

        ## result or answer of this problem, a list, will never have elements more than 32 bcoz we can only do double,
        ## triple, quadruple, etc. and it'll not go beyond 32 times since that's the max we can store (around 4B) and
        ## "1 <= nums[i] <= 2,000,000,000" anyway

        def memoization(idx, prevNum):
            # Base Case
            if idx == n:
                return []

            if (idx, prevNum) in dp:
                return dp[(idx, prevNum)]

            # Explore all cases
            ## Skip the element at idx
            res = memoization(idx+1, prevNum)
            ## Include the element at idx
            if nums[idx] % prevNum == 0:
                # this step will have worst case T.C O(32) bcoz temp will never have length greater than 32
                temp = [nums[idx]] + memoization(idx+1, nums[idx]) # Check for remaining elements in nums
                # update only if it exceeds the length we've until now, since we only need the largest subset
                res = temp if len(temp) > len(res) else res

            dp[(idx, prevNum)] = res
            return res

        # initialize `prevNum` as 1 bcoz that's divisible by every number
        return memoization(0, 1)
