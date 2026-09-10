class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    cache[r][c] = grid[r][c]
                else:
                    left = up = grid[r][c]
                    if c > 0:
                        left += cache[r][c-1]
                    else:
                        left += int(1e9)
                    if r > 0:
                        up += cache[r-1][c]
                    else:
                        up += int(1e9)
                    
                    cache[r][c] = min(left, up)
        
        return cache[m-1][n-1]