class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        dp = {}
        
        # if total sum is odd we can't divide in two equal halve subset (with equal sum)
        if total % 2 != 0:
            return False
        
        ## If there exist a subset whose sum is total/2, then other subset will automatically have sum 
        ## equal to total/2
        target = total//2

        def memo(idx, target):
            # Base cases
            if target == 0:
                return True
            
            if idx == 0:
                return nums[0] == target

            # Memoization
            if (idx,target) in dp:
                return dp[(idx,target)]

            # We can choose the element for required subset only when it's not greater than target itself
            take = memo(idx-1, target - nums[idx]) if target >= nums[idx] else False
            notTake = memo(idx-1, target) # ignore the element at current index

            dp[(idx,target)] = take or notTake
            return dp[(idx,target)]
        
        return memo(n-1, target)
