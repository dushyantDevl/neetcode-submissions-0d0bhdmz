class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            grid[r][c] = 0 # mark visited
            q = deque()
            q.append((r,c))
            area = 0

            while q:
                row, col = q.popleft()
                area += 1

                if row-1 >= 0 and grid[row-1][col] == 1: # Upper land cell
                    q.append((row-1, col))
                    grid[row-1][col] = 0
                if row+1 < ROWS and grid[row+1][col] == 1: # Lower land cell
                    q.append((row+1, col))
                    grid[row+1][col] = 0
                if col-1 >= 0 and grid[row][col-1] == 1: # Left land cell
                    q.append((row, col-1))
                    grid[row][col-1] = 0
                if col+1 < COLS and grid[row][col+1] == 1: # Right land cell
                    q.append((row, col+1))
                    grid[row][col+1] = 0

            return area

        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea