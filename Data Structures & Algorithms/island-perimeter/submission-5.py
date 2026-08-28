class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(row, col):
            que = deque([(row,col)])
            visited.add((row,col))
            perimeter = 0

            while que:
                r, c = que.popleft()
                # Check for all neighbors
                for dr,dc in directions:
                    nxtR, nxtC = r+dr, c+dc

                    # If neighbor is boundary element
                    if (nxtR < 0 or nxtC < 0 or 
                        nxtR >= ROWS or nxtC >= COLS or
                        grid[nxtR][nxtC] == 0
                    ):
                        perimeter += 1

                    elif (nxtR, nxtC) not in visited:
                        que.append((nxtR, nxtC))
                        visited.add((nxtR, nxtC))
            
            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    if (r,c) not in visited:
                        return bfs(r,c)

        return 0           