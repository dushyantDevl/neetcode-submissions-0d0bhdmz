class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: return findMedianSortedArrays(nums2, nums1)
        l, r = 0, m
        left, t = (m+n+1)//2, m+n
        while l <= r:
            m1 = (l+r)//2
            m2 = left - m1
            l1, l2 = -inf