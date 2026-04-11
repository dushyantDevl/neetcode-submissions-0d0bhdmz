class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2, res = len(nums2), []
        for num1 in nums1:
            nge = -1
            for i in range(n2-1, -1, -1):
                if num1 < nums2[i]: nge = nums2[i]
                elif num1 == nums2[i]: break
            res.append(nge)
        return res