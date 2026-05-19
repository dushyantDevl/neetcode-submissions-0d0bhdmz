class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return num
            hashSet.add(num)
        