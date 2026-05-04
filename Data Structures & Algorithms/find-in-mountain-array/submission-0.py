class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        k = 0
        while k != mountainArr.length():
            if mountainArr.get(k) == target: return k
            k += 1
        return -1