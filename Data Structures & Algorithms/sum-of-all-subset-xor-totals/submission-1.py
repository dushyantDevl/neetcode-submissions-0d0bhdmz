class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ## Each element in num will either be included in subset or not, same for their bit representation
        ## i.e each bit in a number will contribute 50-50 for e.g if there are 8 possible subsets
        ## then bit at certain position will be present in 4 of the subsets (i.e. 2**(n-1))
        setBits = 0 # all bits that appear in at least element
        for num in nums:
            setBits |= num
        return setBits << len(nums)-1 # same as setBits * 2**(len(nums)-1)