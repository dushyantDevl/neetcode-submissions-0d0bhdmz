class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        vis = set()

        def bfs(r, c):
            vis.add((r,c))
            q = deque()
            q.append((r,c))

            while q:
                (row, col) = q.popleft()

                # Traverse in the neighbors and mark them if its a land
                ## Up
                if row-1 >= 0 and grid[row-1][col] == '1' and (row-1,col) not in vis:
                    vis.add((row-1,col))
                    q.append((row-1,col))
                ## Right
                if col+1 < COLS and grid[row][col+1] == '1' and (row,col+1) not in vis:
                    vis.add((row,col+1))
                    q.append((row,col+1))
                ## Down
                if row+1 < ROWS and grid[row+1][col] == '1' and (row+1,col) not in vis:
                    vis.add((row+1,col))
                    q.append((row+1,col))
                ## Left
                if col-1 >= 0  and grid[row][col-1] == '1' and (row,col-1) not in vis:
                    vis.add((row,col-1))
                    q.append((row,col-1))


        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in vis and grid[r][c] == '1':
                    res += 1
                    bfs(r,c)

        return res
