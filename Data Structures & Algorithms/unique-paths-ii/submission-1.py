class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0]*n for _ in range(m)]

        # If the start point is blocked, you can't go anywhere.
        if obstacleGrid[0][0] == 1:
            return 0
        
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
                elif r == c == 0:
                    cache[0][0] = 1 # Base cases
                else:
                    left = up = 0
                    if r > 0:
                        up = cache[r-1][c]
                    if c > 0:
                        left = cache[r][c-1]

                    cache[r][c] = left + up

        return cache[m-1][n-1]