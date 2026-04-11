class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx, res, stk = {num1:i for i,num1 in enumerate(nums1)}, [-1] * len(nums1), []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stk and curr > stk[-1]:
                val = stk.pop()
                idx = nums1Idx[val]
                res[idx] = curr
            if curr in nums1Idx:
                stk.append(curr)
        return res