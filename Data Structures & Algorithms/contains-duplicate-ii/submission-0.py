class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Since i starts from 0, size of the window will be `j-i+1` or max length should be k+1
        window, i = set(), 0
        for j in range(len(nums)):
            if j - i > k:
                window.remove(nums[i])
                i += 1
            if nums[j] in window: return True
            window.add(nums[j])
        return False