class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [x for x in candidates if x <= target]
        candidates.sort()
        res, temp = [], []

        def backtrack(idx, n, total):
            if total == target:
                res.append(temp.copy())
                return
            
            if total > target or idx == n:
                return
            
            # Include candidates
            temp.append(candidates[idx])
            backtrack(idx+1, n, total+candidates[idx])
            temp.pop()

            # Skip duplicate candidates
            while idx+1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx+1, n, total)

        backtrack(0, len(candidates), 0)
        
        return res