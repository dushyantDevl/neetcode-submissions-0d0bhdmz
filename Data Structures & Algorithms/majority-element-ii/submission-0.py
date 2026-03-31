class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_freq, res = {}, []
        for num in nums: num_freq[num] = num_freq.get(num, 0) + 1
        for key,val in num_freq.items():
            if val>(len(nums)//3):
                res.append(key)
        return res