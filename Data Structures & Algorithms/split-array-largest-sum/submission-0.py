class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if n < k: return -1
        
        def allocate(subArraySum):
            NoSubArray, currSum = 1, 0 # subarray-1 holding 0 subArraySum right now
            for i in range(n):
                if currSum + nums[i]  <= subArraySum:
                    currSum += nums[i]
                else: 
                    # go to next subarray and allocate the current number that couldn't be allocated
                    NoSubArray, currSum = NoSubArray+1, nums[i]
            return NoSubArray
        
        minSum, MaxSum = nums[0], nums[0]
        for i in range(1, n):
            minSum = max(minSum, nums[i])
            MaxSum += nums[i]
            
        l, r = minSum, MaxSum
        
        while l <= r:
            m = (l+r)//2
            NoSubArray = allocate(m)
            if NoSubArray > k: l = m+1
            else: r = m-1
        
        return l