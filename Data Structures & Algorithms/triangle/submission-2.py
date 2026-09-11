class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Top-Down Approach (recursion + dp)
        m = len(triangle)
        dp = [[None]*(i+1) for i in range(m)]

        def memo(i, j): 
            if i == m-1: # reached to last row (destination)
                return triangle[i][j]
            
            if dp[i][j] != None:
                return dp[i][j]

            down = triangle[i][j] + memo(i+1, j)
            diagonallyDown = triangle[i][j] + memo(i+1, j+1)

            dp[i][j] = min(down, diagonallyDown)
            return dp[i][j]

        return memo(0,0)