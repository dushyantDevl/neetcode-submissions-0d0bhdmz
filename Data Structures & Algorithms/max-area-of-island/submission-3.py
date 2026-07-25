class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def bfs(r,c):
            grid[r][c] = 0 # mark visited
            q = deque()
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == 0
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1

            return area

        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r,c))

        return maxArea