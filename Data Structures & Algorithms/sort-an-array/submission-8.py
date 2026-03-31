class Solution:
    def _merge(self, l_idx:int, m_idx:int, r_idx:int, arr:List[int]) -> None:
        L, R = arr[l_idx:m_idx+1], arr[m_idx+1:r_idx+1]
        i, j, k = l_idx, 0, 0 # i for in-place insertion in arr, j & k for L & R
        while j<len(L) and k<len(R) :
            if L[j] < R[k]:
                arr[i] = L[j]
                j += 1
            else:
                arr[i] = R[k]
                k += 1
            i += 1
        while j<len(L):
            arr[i] = L[j]
            j += 1
            i += 1
        while k<len(R):
            arr[i] = R[k]
            k += 1
            i += 1

    def _mergeSort(self, l_idx:int, r_idx:int, arr:List[int]) -> List[int]:
        if l_idx == r_idx:
            return arr
        m_idx = (l_idx+r_idx)//2
        self._mergeSort(l_idx, m_idx, arr)
        self._mergeSort(m_idx+1, r_idx, arr)
        self._merge(l_idx, m_idx, r_idx, arr)
        return arr
        
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._mergeSort(0, len(nums)-1, nums)
        