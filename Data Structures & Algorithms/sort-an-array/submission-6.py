class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion Sort
        nums_len = len(nums)
        for i in range(1, nums_len):
            key, j = nums[i], i-1
            while(j>=0):
                if nums[j]>key:
                    nums[j+1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j+1] = key
        return nums