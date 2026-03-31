class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Hint: At most only 2 elements can have frequency greater than n//3
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num==candidate1: count1 += 1
            elif num==candidate2: count2 += 1
            elif count1==0:
                candidate1 = num
                count1 = 1
            elif count2==0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res, count1, count2 = [], 0, 0
        for num in nums:
            if num==candidate1: count1 += 1
            elif num==candidate2: count2 += 1
        if count1 > len(nums)//3: res.append(candidate1)
        if count2 > len(nums)//3: res.append(candidate2)
        return res