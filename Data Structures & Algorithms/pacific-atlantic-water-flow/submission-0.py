class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Go from Ocean to cell (reverse method)
        ## Starting from boundary cells -> we've to check for opposite condition
        ## i.e. from ocean to cells of increasing value (not decreasing since its reverse)
        ROWS, COLS = len(heights), len(heights[0])
        inPacific, inAtlantic = set(), set()

        def dfs(r, c, oceanVisit, prevHeight):
            if ((r,c) in oceanVisit or
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight
            ):
                return
            
            oceanVisit.add((r,c))

            # Check for all 4 adjacent cells (if water can flow there)
            dfs(r+1, c, oceanVisit, heights[r][c])
            dfs(r-1, c, oceanVisit, heights[r][c])
            dfs(r, c+1, oceanVisit, heights[r][c])
            dfs(r, c-1, oceanVisit, heights[r][c])
        
        # Check for boundary Rows i.e. 0th and (ROWS-1)th
        for c in range(COLS):
            dfs(0, c, inPacific, heights[0][c])
            dfs(ROWS-1, c, inAtlantic, heights[ROWS-1][c])

        # Check for boundary Columns i.e. 0th and (COLS-1)th
        for r in range(ROWS):
            dfs(r, 0, inPacific, heights[r][0])
            dfs(r, COLS-1, inAtlantic, heights[r][COLS-1])

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in inPacific and (r, c) in inAtlantic:
                    res.append([r,c])

        return res
        
