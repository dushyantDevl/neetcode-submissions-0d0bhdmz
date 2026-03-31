class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k, res = 0, 0, 0, [0]*(m+n)
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i, k = i+1, k+1
            else:
                res[k] = nums2[j]
                j, k = j+1, k+1
        while i<m:
            res[k] = nums1[i]
            i, k = i+1, k+1
        while j<n:
            res[k] = nums2[j]
            j, k = j+1, k+1
        nums1[:] = res