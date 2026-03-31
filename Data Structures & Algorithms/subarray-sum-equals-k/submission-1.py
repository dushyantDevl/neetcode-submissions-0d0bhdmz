class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrayFreq, prefixSum, res = {0:1}, 0, 0
        for num in nums:
            prefixSum += num
            diff = prefixSum-k
            if diff in subarrayFreq:
                res += subarrayFreq[diff]
            subarrayFreq[prefixSum] = subarrayFreq.get(prefixSum,0)+1
        return res