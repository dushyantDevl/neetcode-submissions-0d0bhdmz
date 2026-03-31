class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection Sort
        nums_len = len(nums)
        for i in range(nums_len):
            min_idx = i
            for j in range(i+1, nums_len):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums