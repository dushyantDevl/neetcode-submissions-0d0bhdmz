class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq =  collections.deque() # stores index
        l = r = 0

        while r < len(nums):
            # pop smaller values from window (dq), since those can never be maximum
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]: # remove left pointer index when we shift to right from it
                dq.popleft()

            if (r+1) >= k: # when window size is atleast k
                res.append(nums[dq[0]])
                l += 1
            
            r += 1

        return res