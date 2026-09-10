class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1]*n for _ in range(m)]

        def dp(r, c):
            # If it's a obstacle, we cant include that cell in a path
            if r >= 0 and c >= 0 and obstacleGrid[r][c] == 1:
                return 0

            # Out of boundary condition
            if r < 0 or c < 0:
                return 0

            # Destination reached
            if r == c == 0:
                return 1

            # Memoization
            if cache[r][c] != -1:
                return cache[r][c]

            left = dp(r, c-1)
            up = dp(r-1, c)

            cache[r][c] = left + up
            return cache[r][c]
            
        return dp(m-1, n-1)
