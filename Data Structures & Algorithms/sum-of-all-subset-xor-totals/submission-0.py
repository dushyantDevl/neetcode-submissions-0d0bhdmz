class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subsetXORSumRecursively(i, n, total):
            if i >= n: return total
            return  subsetXORSumRecursively(i+1, n, total^nums[i]) + subsetXORSumRecursively(i+1, n, total)
        return subsetXORSumRecursively(0, len(nums), 0)
