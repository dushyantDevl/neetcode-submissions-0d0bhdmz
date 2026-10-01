class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def memo(idx):
            # Base Case
            if idx == 0:
                ## if there's just one element in list, it can be a part of both increasing or 
                ## decreasing sequence
                return 1

            if dp[idx] != -1:
                return dp[idx]

            ## since it's a subsequence (not substring), we can consider the case when we choose
            ## not to take any element and still form a subsequence
            take = memo(idx-1)

            notTake = 0
            if idx > 0 and nums[idx] > nums[idx-1]: # increasing condition
                ## count the current element if it's a part of increasing subsequence then go 
                ## search in the remaining list
                notTake = 1 + memo(idx-1)
            else:
                ## when there's no increasing subsequence or some element broke the chain, just 
                ## don't count that element without starting from 1 again bcoz it's possible to
                ## continue with the required condition if we find the suitable element later
                notTake = memo(idx-1)

            dp[idx] = max(notTake, take)
            return dp[idx]

        return memo(n-1)