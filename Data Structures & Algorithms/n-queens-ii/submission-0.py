class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set() # row - col will remain constant (since row and col both are increasing)
        posDiag = set() # row + col will remain constant (since row is decreasing and col is increasing)

        board = [['.'] * n for i in range(n)] # empty board
        res = []

        def backtrack(r):
            if r == n: # reached to last row
                boardCopy = ["".join(row) for row in board]
                res.append(boardCopy)
                return

            for c in range(n): # c represent each column number (from 0 to n-1)
                if c in col or (r-c) in negDiag or (r+c) in posDiag: # invalid move conditions
                    continue

                # place the queen
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = 'Q'

                backtrack(r+1)

                # Remove to check for next row
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."

        backtrack(0)
        return len(res)