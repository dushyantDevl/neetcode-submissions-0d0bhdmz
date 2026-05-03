class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, m
        left, t = (m+n+1)//2, m+n
        while l <= r:
            m1 = (l+r)//2
            m2 = left - m1
            
            l1, l2 = -math.inf, -math.inf
            r1, r2 = math.inf, math.inf

            if m1 < m: r1 = nums1[m1]
            if m2 < n: r2 = nums2[m2]
            if m1-1 >= 0: l1 = nums1[m1-1]
            if m2-1 >= 0: l2 = nums2[m2-1]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2) if t%2==1 else (max(l1,l2) + min(r1,r2)) / 2.0
            elif l1 > l2: r = m1-1
            else: l = m1+1