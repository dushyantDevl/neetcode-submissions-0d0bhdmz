class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSortedList(l, mid, r):
            L, R = nums[l:mid+1], nums[mid+1:r+1]
            i, j, k = 0, 0, l

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
                

        def mergeSort(l, r):
            if l >= r:
                return

            mid = (l + r) // 2

            mergeSort(l, mid)
            mergeSort(mid + 1, r)

            mergeSortedList(l, mid, r)

        mergeSort(0, len(nums)-1)
        return nums
        
