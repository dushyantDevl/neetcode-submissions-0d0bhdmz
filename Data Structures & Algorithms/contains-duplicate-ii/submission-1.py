class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            # check if the current value at i was already present in map
            if nums[i] in map:
                # map still has older index stored in it so we can check for required condition
                # before updating the index in last line of this for-loop block
                if abs(i - map[nums[i]]) <= k: return True 
            map[nums[i]] = i # store each value, `i` will be updated to new index in case of duplicate
        return False