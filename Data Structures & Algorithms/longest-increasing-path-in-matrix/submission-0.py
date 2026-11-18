class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        dp = [[-1]*COLS for _ in range(ROWS)]

        ## Since the problem ask for longest STRICTLY increasing path, we don't have to worry about stuck 
        ## in a a loop while traversing i.e. we don't have to track the visited element since at each 
        ## matrix cell we'll only move in STRICTLY increasing directions (no way of going back to where we
        ## came from)

        def memoization(r,c):
            if dp[r][c] != -1:
                return dp[r][c]

            res = 1  # the cell itself is a path of length 1
            for dr,dc in directions:
                rdr, cdc = (r+dr), (c+dc)
                # run recursion only for valid moves and when next cell has greater number
                # checking for valid moves here also means there's no need of base case at the top
                if 0 <= (rdr) < ROWS and 0 <= (cdc) < COLS and matrix[r][c] < matrix[rdr][cdc]:
                    res = max(res, 1 + memoization(rdr, cdc))

            dp[r][c] = res
            return res

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, memoization(r,c))

        return res