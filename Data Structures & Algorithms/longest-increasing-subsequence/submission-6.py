from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ## store elements from `nums` in increasing order, not necessarily a subsequence tho since we just want the 
        ## max length not exact subsequence
        temp, res = [nums[0]], 1

        for i in range(1, n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                res += 1
            else:
                ## find the index of the element in `temp` which is either equal to `nums[i]` or the first greater (than
                ## nums[i]) from left
                firstLeftGreaterElementIdx = bisect_left(temp, nums[i])
                ## to keep the `temp` sorted (increasing) replace from the new element in `nums`
                temp[firstLeftGreaterElementIdx] = nums[i]

        return res # or len(temp)

    '''DRY run
    nums = [9,1,4,2,3,3,7], n = 7, temp = [9]
    @ i=1 => 1 < 9 therefore, firstLeftGreaterElementIdx = 0 => temp = [1], res = 1
    @ i=2 => 4 > 1 => temp = [1,4], res = 2
    @ i=3 => 2 < 4 therefore, firstLeftGreaterElementIdx = 1 => temp = [1,2], res = 2
    @ i=4 => 3 > 1 => temp = [1,2,3], res = 3
    @ i=5 => 3 = 3 therefore, firstLeftGreaterElementIdx = 2 => temp = [1,2,3], res = 3
    @ i=6 => 7 > 3 => temp = [1,2,3,7], res = 4
    return `4 `. [1,2,3,7] isn't a even a subsequence but its length is lengthOfLIS
    '''