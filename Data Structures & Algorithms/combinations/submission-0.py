class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, temp = [], []

        def backtrack(num, n):
            if num > n:
                res.append(temp.copy())
                return

            temp.append(num)
            backtrack(num+1, n)
            temp.pop()

            backtrack(num+1, n)
        
        backtrack(1, n)

        return [x for x in res if len(x)==k]