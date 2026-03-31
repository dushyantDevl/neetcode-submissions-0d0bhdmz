class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm
        ## Intution: majority element will appear more than any other element combined
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if res==num else -1
        return res