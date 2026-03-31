import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high) -> int:
            rand_idx = random.randint(low, high)
            nums[low], nums[rand_idx] = nums[rand_idx], nums[low]
            pivot, i, j = nums[low], low, high

            while i<j :
                while nums[i]<=pivot and i<=high-1 : i += 1 
                while nums[j]>pivot and j>=low+1 : j -= 1
                if i<j : nums[i], nums[j] = nums[j], nums[i]

            nums[low], nums[j] = nums[j], nums[low]
            return j
        
        def quickSort(nums, low, high):
            if low < high:
                partitionIndex = partition(nums, low, high)
                quickSort(nums, low, partitionIndex-1)
                quickSort(nums, partitionIndex+1, high)

        quickSort(nums, 0, len(nums)-1)

        return nums

