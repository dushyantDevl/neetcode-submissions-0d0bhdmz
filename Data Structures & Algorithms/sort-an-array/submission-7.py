class Solution:
    def _merge_sorted_list(self, nums: List[int], start: int, mid: int, end: int):
        first_half_size = mid-start+1
        first_half_copy = [0] * first_half_size
        second_half_size = end-mid
        second_half_copy = [0] * second_half_size

        for i in range(first_half_size): first_half_copy[i] = nums[start+i]
        for j in range(second_half_size): second_half_copy[j] = nums[mid+1+j]

        i=j=0
        k=start

        while(i<first_half_size and j<second_half_size):
            if (first_half_copy[i] < second_half_copy[j]):
                nums[k] = first_half_copy[i]
                i += 1
            else:
                nums[k] = second_half_copy[j]
                j += 1
            k += 1

        while(i<first_half_size):
            nums[k] = first_half_copy[i]
            i += 1
            k += 1
        while(j<second_half_size):
            nums[k] = second_half_copy[j]
            j += 1
            k += 1
    
    def _divide_list(self, start: int, end: int, nums: List[int]):
        if start >= end:
            return
        mid = (start+end)//2
        self._divide_list(start, mid, nums)
        self._divide_list(mid+1, end, nums)
        self._merge_sorted_list(nums, start, mid, end)


    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort
        self._divide_list(0, len(nums)-1, nums)
        return nums