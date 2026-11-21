class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        X, Y = len(grid), len(grid[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)] # [up, right, down, left]

        def bfs(x,y):
            grid[x][y] = "0" # mark visited
            
            q = deque([(x,y)])

            while q:
                currLandX, currLandY = q.popleft()
                
                for dx,dy in directions:
                    adjacentLandX, adjacentLandY = currLandX+dx, currLandY+dy
                    if 0 <= adjacentLandX < X and 0 <= adjacentLandY < Y and grid[adjacentLandX][adjacentLandY] == "1":
                        grid[adjacentLandX][adjacentLandY] = "0" # mark visited
                        q.appendleft((adjacentLandX, adjacentLandY))



        res = 0
        for x in range(X):
            for y in range(Y):
                # run bfs only for land
                if grid[x][y] == "1":
                    bfs(x,y)
                    res += 1

        return res
