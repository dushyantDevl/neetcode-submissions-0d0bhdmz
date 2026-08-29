class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * (len(nums))

        def dp(idx): # returns max sum from last house (i=n-1) to 1st house (i=0)
            if idx == 0:
                ## If we've reached at this index (last index can't be 1)
                ## we've to choose this house too for maximizing rob amount
                return nums[0]

            if idx < 0:
                return 0

            if cache[idx] != -1:
                return cache[idx]

            ## If thief decides to rob house at idx then it can't go to the next 
            ## one i.e. idx-1 so go to next to next instead i.e idx-2
            choose = nums[idx] + dp(idx-2)

            ## If thief decides not to rob house at idx then it can choose the next 
            ## one i.e. idx-1
            Notchoose = 0 + dp(idx-1)

            cache[idx] = max(choose, Notchoose)

            return cache[idx]

        return dp(len(nums)-1)