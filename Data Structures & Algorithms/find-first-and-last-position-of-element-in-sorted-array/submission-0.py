class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstOccurence = lastOccurence = -1
        i, n, firstOccurenceFound = 0, len(nums), False
        while i < n:
            if nums[i] == target:
                if not firstOccurenceFound:
                    firstOccurence = i
                    firstOccurenceFound = True
                lastOccurence = i
                if i+1 < n and nums[i+1] != target: break
            i += 1
        return [firstOccurence, lastOccurence]