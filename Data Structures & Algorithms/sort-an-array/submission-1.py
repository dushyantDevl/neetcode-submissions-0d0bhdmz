class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Bubble Sort
        nums_len = len(nums)
        flag = False
        for i in range(nums_len):
            for j in range(0, nums_len-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = True
            if not flag:
                break
        return nums