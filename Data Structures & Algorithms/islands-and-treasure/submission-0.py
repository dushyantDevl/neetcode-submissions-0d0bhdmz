class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Reverse approach
        ## Start BFS from all treasure chest cell at the same time, it'll mark smallest 
        ## min. distance to the closest land cell

        ROWS, COLS = len(grid), len(grid[0])
        vis = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                # Put all the treasure cell in queue to start BFS from there
                if grid[r][c] == 0:
                    vis.add((r,c))
                    q.append((r,c))

        dist = 0 # initial distance from treasure cell (0 from itself)

        def addValidCell(r,c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in vis or
                grid[r][c] == -1 # water cell that can not be traversed.
            ):
                return

            vis.add((r,c))
            q.append((r,c))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                # Add all valid cells from all 4 direction
                addValidCell(r+1, c)
                addValidCell(r-1, c)
                addValidCell(r, c+1)
                addValidCell(r, c-1)

            dist += 1 # update distance when going to 2nd set of valid cells
