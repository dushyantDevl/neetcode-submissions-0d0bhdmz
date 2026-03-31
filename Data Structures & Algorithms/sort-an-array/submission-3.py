class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection Sort
        nums_len = len(nums)
        for i in range(nums_len):
            min, min_i= nums[i], i
            for j in range(i+1, nums_len):
                if min > nums[j]:
                    min = nums[j]
                    min_i = j
            nums[i], nums[min_i] = nums[min_i], nums[i]
        return nums