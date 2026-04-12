# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        temp, l, r = [x for x in range(1,n+1)], 0, n-1
        while l <= r:
            mid = (l+r)//2
            if guess(temp[mid]) == 0: return temp[mid]
            elif guess(temp[mid]) == -1: r = mid-1
            else: l = mid+1