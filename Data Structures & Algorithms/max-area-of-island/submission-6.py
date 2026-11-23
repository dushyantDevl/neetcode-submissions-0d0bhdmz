class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COlS = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]

        def bfs(r,c):
            q = deque([(r,c)])

            grid[r][c] = 0 # mark visited (first land cell where bfs is called)
            area = 1 # for current land cell

            while q:
                row, col = q.popleft()

                for dr,dc in directions:
                    rdr, cdc = row+dr, col+dc
                    if 0 <= rdr < ROWS and 0 <= cdc < COlS and grid[rdr][cdc] == 1:
                        grid[rdr][cdc] = 0 # mark visited (neighbor land)
                        area += 1
                        q.appendleft((rdr,cdc)) # add area of valid land cells
            
            return area
        
        maxArea = 0

        for r in range(ROWS):
            for c in range(COlS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea