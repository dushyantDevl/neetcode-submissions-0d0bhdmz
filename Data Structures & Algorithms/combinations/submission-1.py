class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, temp = [], []

        def backtrack(num, n, k):
            if len(temp) == k: 
                res.append(temp.copy())
                return

            if num > n:
                return

            temp.append(num)
            backtrack(num+1, n, k)
            temp.pop()

            backtrack(num+1, n, k)
        
        backtrack(1, n, k)

        return res