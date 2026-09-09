class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top-Down Approach (from bottom-right corner to top-left corner)
        ## therefore we can only move either up or to the left 
        
        ## When you use the * operator to multiply a list that contains another list, 
        ## Python doesn't create independent rows. Instead, it creates m references to the 
        ## exact same list.
        # cache = [[-1] * n] * m 

        # FIXED: Use list comprehension to create independent rows
        cache = [[-1] * n for _ in range(m)]

        def dp(r, c): # no. of unique ways to reach from top-left corner to (r,c)
            if r == 0 and c == 0: # destination reached
                return 1
            if r < 0 or c < 0: # out of grid, cant be count as any path
                return 0

            if cache[r][c] != -1:
                return cache[r][c]

            up = dp(r-1, c)
            left = dp(r, c-1)

            cache[r][c] = up + left
            return cache[r][c]

        return dp(m-1, n-1)
        
        # T.C:
        ## With Recursion: $O(2^{m \times n})$
        ## With memoization: $O(m \times n)$
        # S.C:
        ## With Recursion: O(path length) => $O((m-1) + (n-1))$
        ## ## With memoization: $O((m-1) + (n-1)) + O(m \times n)$