class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, hashSet, res = len(nums), set(nums), None
        # Hint: answer will surely be in [1,n+1], since 1 is smallest positive integer and 
        # in worst case if nums contain all integer from 1 to n then answer will be n+1,
        # checking consecutively
        for num in range(1,n+2):
            if num not in hashSet: return num