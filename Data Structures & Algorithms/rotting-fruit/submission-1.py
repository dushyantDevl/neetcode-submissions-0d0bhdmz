class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time, freshFruit = 0, 0
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        def validCell(r, c):
            # Valid iff r,c are in bounds and have fresh fruit
            if (r<0 or r>=ROWS or 
                c<0 or c>=COLS or
                grid[r][c] != 1
            ):
                return
            
            # Make the fruit rotten and include in que to check for next set of fruits
            grid[r][c] = 2
            q.append((r,c))

            nonlocal freshFruit
            freshFruit -= 1

        # run BFS on all the rotten fruits together
        while q and freshFruit > 0: # no need to check for fruits if all are already rotten
            for _ in range(len(q)):
                i, j = q.popleft()

                # Check for all the adjacent cells
                validCell(i+1, j)
                validCell(i-1, j)
                validCell(i, j+1)
                validCell(i, j-1)
            
            time += 1

        return time if freshFruit == 0 else -1
        