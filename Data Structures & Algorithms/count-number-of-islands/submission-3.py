class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        direction = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]

        def bfs(r, c):
            visited.add((r, c))
            q = deque()
            q.append((r,c))

            while q:
                (row, col) = q.popleft()
                
                for (dr,dc) in direction:
                    neighborRow, neighborCol = row+dr, col+dc

                    if (0 <= neighborRow < m and 0 <= neighborCol < n and # valid cells
                        grid[neighborRow][neighborCol] == '1' and # only check for land
                        (neighborRow, neighborCol) not in visited): # mark only once
                            visited.add((neighborRow, neighborCol))
                            q.append((neighborRow, neighborCol))


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    res += 1 

        return res                    