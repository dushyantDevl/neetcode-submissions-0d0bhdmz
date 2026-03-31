class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0 or n==1: return n
        nums = sorted(nums)
        longest_sequence = 1
        for i in range(n):
            num, temp_count = nums[i], 1
            for j in range(i+1,n):
                if nums[j] == num+1:
                    num += 1
                    temp_count += 1
            if temp_count>longest_sequence:
                longest_sequence = temp_count
        return longest_sequence