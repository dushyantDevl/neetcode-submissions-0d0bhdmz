class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largestSum):
            noOfSubarray, currSum = 1, 0 # 1st subarray having sum=0 (initially before iterating)
            for num in nums:
                currSum += num
                if currSum > largestSum:
                    noOfSubarray += 1
                    currSum = num
            return noOfSubarray <= k
        
        while l <= r:
            m = l + (r-l)//2
            if canSplit(m):
                res = m
                r = m-1
            else:
                l = m+1
        
        return res