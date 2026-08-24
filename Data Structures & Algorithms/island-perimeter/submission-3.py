class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    islands += 1
        
        return (islands-2)*2 + 2*3