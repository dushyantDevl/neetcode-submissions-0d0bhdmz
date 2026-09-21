class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            minTime = 0
            
            ## Do the traversal via BFS bcoz that travels level wise and it can be used to find
            ## the minimum time bcoz it travels to all neighbor cell at once unlike DFS which 
            ## goes step by step
            q = deque() # (row, col, time): time at which the particular fruit is rotten
            visited = set()
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            # Put all the rotten orange positions first in the queue (to start BFS from)
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        q.append((i, j, minTime))
                        visited.add((i,j))
                        
            time = 0
            while q:
                i, j, time = q.popleft()
                minTime = max(minTime, time)
                
                for di,dj in directions:
                    ni, nj = i+di, j+dj
                    
                    # Check for valid positions only: not out of boundary, not visited, is fresh
                    if (
                        0 <= ni < m and 0 <= nj < n and
                        (ni,nj) not in visited and
                        grid[ni][nj] == 1
                    ):
                        q.append((ni, nj, time+1))
                        visited.add((ni,nj))
                        
            # Check if fresh oranges left in grid
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i,j) not in visited:
                        return -1
                        
            return minTime