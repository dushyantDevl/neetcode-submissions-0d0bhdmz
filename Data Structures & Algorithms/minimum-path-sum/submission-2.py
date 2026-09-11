class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prevRow = [0]*n

        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    prevRow[c] = grid[r][c]
                else:
                    left = up = grid[r][c]
                    
                    # requires current row's 'c-1' column
                    if c > 0:
                        left += prevRow[c-1]
                    else:
                        left += int(1e9)
                    
                    # requires previous row's 'c' column
                    if r > 0:
                        up += prevRow[c]
                    else:
                        up += int(1e9)
                    
                    prevRow[c] = min(left, up)
        
        return prevRow[n-1]