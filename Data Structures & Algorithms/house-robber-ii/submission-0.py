class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRobber1(nums):
            rob1 = rob2 = 0

            for num in nums:
                ## If theif robs house *num* then it can also select last to 
                ## last house i.e. rob1
                choose = num + rob1
                skip = rob2 # last house can be robbed if current one isn't selected
                
                curr = max(choose, skip)
                
                ## procced and also updates the last 2 variable
                rob1 = rob2
                rob2 = curr

            return rob2
        
        ## max of both the cases, when thief robs 1st house (except the last) 
        ## and when thief robs last house (except the first house)
        return max(houseRobber1(nums[:-1]), houseRobber1(nums[1:]))