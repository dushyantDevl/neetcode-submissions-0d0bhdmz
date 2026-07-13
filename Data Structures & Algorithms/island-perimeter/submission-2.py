class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                # Check only for the cells that are part of island (or itself a island)
                if grid[r][c]:
                    perimeter += 4 # single island in middle of water -> max perimeter of cell

                    ## Since we're traversing all columns of particular row from left to right 
                    ## and then same for next row, no need to check for right and down side of cell
                    
                    # Check for Top cell
                    if r > 0 and grid[r-1][c]: # both above and current cell shares an edge
                        perimeter -= 2

                    # Check for Left cell
                    if c > 0 and grid[r][c-1]: # both left and current cell shares an edge
                        perimeter -= 2

        return perimeter