class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        lookup, longest = set(nums), 1
        for num in nums:
            # starting no. in sequence will not going to have any left neighbor
            if num-1 not in lookup:
                temp = 1
                while num+temp in lookup:
                    temp += 1
                longest = max(temp, longest)
        return longest