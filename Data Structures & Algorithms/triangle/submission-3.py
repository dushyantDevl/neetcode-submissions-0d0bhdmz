class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = [[0]*(i+1) for i in range(m)]

        # Base case 
        ## starting from last row of triangle, tho it'd be tough to start from last row in case of
        ## recursion that's why we started from 1st row (fixed single element) which is a bit different
        ## how we most of the time start from last to first row in recursion solution, so now for the
        ## tabulation method we'll do the opposite and start from last row (so for base case make the last
        ## row of dp same as triangle)
        for i in range(m):
            dp[m-1][i] = triangle[m-1][i]

        # since last row is filled, go from 2nd last to 1st row
        for i in range(m-2, -1, -1):
            ## going down, no. of element increases is same as current row number
            ## i.e. 1st row has 1 element, 2nd has 2, 3rd has 3 and so on, that's why column number
            ## starts from `i` (going from last to 1st row)
            for j in range(i, -1, -1):
                down = triangle[i][j] + dp[i+1][j] 
                diagonallyDown = triangle[i][j] + dp[i+1][j+1] 
                dp[i][j] = min(down, diagonallyDown)
        
        return dp[0][0]
        