class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0 or n==1: return n
        nums = sorted(nums)
        longest_sequence, temp_count = 1, 1
        for i in range(n):
            if i+1<n and nums[i+1] == nums[i]: continue
            elif i+1<n and nums[i+1] == nums[i]+1:
                temp_count += 1
            else:
                if temp_count>longest_sequence:
                    longest_sequence = temp_count
                temp_count = 1
        return longest_sequence