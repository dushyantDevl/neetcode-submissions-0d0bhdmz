class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]
        
        def bfs(r,c):
            q = deque([(r,c)])
            grid[r][c] = -1 # mark visited
            res = 0

            while q:
                currLandR, currLandC = q.popleft()

                # Check for all the adjacent land
                for dr,dc in directions:
                    adjacentAreaR, adjacentAreaC = currLandR+dr, currLandC+dc

                    # if adjacent area is either either out of boundary or water, add a unit in perimeter
                    if (
                        (adjacentAreaR < 0 or adjacentAreaR >= ROWS) or # out of vertical boundary
                        (adjacentAreaC < 0 or adjacentAreaC >= COLS) or # out of horizontal boundary
                        (grid[adjacentAreaR][adjacentAreaC] == 0) # water area
                    ):
                        res += 1
                    
                    # if area isn't visited before mark it as visited and push to queue
                    elif grid[adjacentAreaR][adjacentAreaC] != -1:
                        grid[adjacentAreaR][adjacentAreaC] = -1 # mark visited
                        q.append((adjacentAreaR, adjacentAreaC))
            
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # bcoz there is exactly one island, we can return directly here
                    return bfs(r,c)

        return 0