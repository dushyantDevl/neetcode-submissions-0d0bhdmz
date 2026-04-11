class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        stk, res, map2 = [], [], {}
        for i in range(n2-1,-1,-1):
            num2 = nums2[i]
            while stk and num2 > stk[-1]:
                stk.pop()
            if not stk:
                map2[num2] = -1
            else:
                map2[num2] = stk[-1]
            stk.append(num2)
        for num1 in nums1: res.append(map2[num1])
        return res