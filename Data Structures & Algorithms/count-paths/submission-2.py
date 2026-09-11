class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        
        # Tabulation (Bottom-up)
        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    prevRow[0] = 1 # base case
                elif c > 0:
                    # prevRow[c] is 'up', prevRow[c-1] is 'left'
                    prevRow[c] += prevRow[c-1]
        
        return prevRow[n-1]
        
        # T.C: $O(m \times n)$
        # S.C: O(m \times n)$