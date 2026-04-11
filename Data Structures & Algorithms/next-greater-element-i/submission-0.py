class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        stk, res1, res2 = [], [0]*n1, [0]*n2
        for i in range(n2-1,-1,-1):
            num2 = nums2[i]
            while stk and num2 > stk[-1]:
                stk.pop()
            if not stk:
                res2[i] = -1
            else:
                res2[i] = stk[-1]
            stk.append(num2)
        
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    res1[i] = res2[j]
        return res1