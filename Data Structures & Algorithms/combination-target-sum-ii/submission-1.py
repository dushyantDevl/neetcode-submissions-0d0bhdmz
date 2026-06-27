class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [x for x in candidates if x <= target]
        candidates.sort()
        res, ds = [], []

        def backtrack(idx, n, target):
            if target == 0:
                res.append(ds.copy())
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]: continue
                if candidates[i] > target: break
                ds.append(candidates[i])
                backtrack(i+1, n, target-candidates[i])
                ds.pop()
        
        backtrack(0, len(candidates), target)
        return res