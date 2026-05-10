class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort arr on the basis of distance from `x`
        arr.sort(key=lambda num: (abs(num-x), num))
        # return the subarray of first k elements
        return sorted(arr[:k])