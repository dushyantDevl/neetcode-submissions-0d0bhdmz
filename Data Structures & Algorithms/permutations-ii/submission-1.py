class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, currPermute = [], []
        freq = {num:0 for num in nums}
        for num in nums: freq[num] += 1

        def backtrack():
            if len(currPermute) == len(nums):
                res.append(currPermute.copy())
                return

            for num in freq:
                if freq[num] > 0:
                    freq[num] -= 1
                    currPermute.append(num)

                    backtrack()

                    freq[num] += 1
                    currPermute.pop()

        backtrack()
        return res