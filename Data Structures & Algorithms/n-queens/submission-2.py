class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)] # Empty board

        leftRow, posDiag, negDiag = set(), set(), set()

        def solve(col):
            if col == n:
                res.append([''.join(row) for row in board])
                return

            for row in range(n):
                if row not in leftRow and (row+col )not in posDiag and (col-row) not in negDiag:
                    board[row][col] = 'Q'
                    leftRow.add(row)
                    posDiag.add(row+col)
                    negDiag.add(col-row)

                    solve(col+1)

                    board[row][col] = '.'
                    leftRow.remove(row)
                    posDiag.remove(row+col)
                    negDiag.remove(col-row)

        solve(0)

        return res