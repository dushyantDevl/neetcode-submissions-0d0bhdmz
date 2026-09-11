class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        
        # Tabulation (Bottom-up)
        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    cache[0][0] = 1 # base case
                else:
                    up = left = 0
                    if r > 0:
                        up = cache[r-1][c]
                    if c > 0:
                        left = cache[r][c-1]
                    
                    cache[r][c] = up + left
        
        return cache[m-1][n-1]
        
        # T.C: $O(m \times n)$
        # S.C: O(m \times n)$