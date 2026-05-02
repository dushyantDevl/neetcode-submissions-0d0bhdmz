class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, i, j, temp = len(nums1), len(nums2), 0, 0, []
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < m: 
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1
        
        t = len(temp)
        return temp[(t-1)//2] if t % 2 == 1 else (temp[(t-1)//2] + temp[((t-1)//2)+1]) / 2