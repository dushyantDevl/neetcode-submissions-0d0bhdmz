class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [0]*n
        cache[0] = 1 # Base cases

        # If the start point is blocked, you can't go anywhere.
        if obstacleGrid[0][0] == 1:
            return 0
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    cache[c] = 0
                elif c > 0:
                    # cache[c] is 'up', cache[c-1] is 'left'
                    cache[c] += cache[c-1]

        return cache[n-1]