class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, temp = [], []
        def backtrack(i, n, target):
            # no need to make further recursion calls if we already got the required combination
            if target == 0:
                res.append(temp.copy())
                return
            if i >= n: 
                return
            
            if nums[i] <= target:
                temp.append(nums[i])
                backtrack(i, n, target-nums[i]) # pick again if satisfies the condition
                temp.pop() # remove the picked one to go the non-pick case
            
            backtrack(i+1, n, target)

        backtrack(0, len(nums), target)
        return res