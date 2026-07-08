class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)] # Empty board

        def solve(col):
            if col == n:
                res.append([''.join(row) for row in board])
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row][col] = 'Q'
                    solve(col+1)
                    board[row][col] = '.'


        # Since we're filling the board starting from left column wise we don't have to check for
        # the upcoming positions i.e. in upper-left, right and lower positions
        def isSafe(row, col):
            tempRow, tempCol = row, col

            # Chek in upper diagonal positions (positive slope diagonal)
            while row >= 0 and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row, col = row-1, col-1

            row, col = tempRow, tempCol
            
            # Check in all the left positions (horizontally)
            while col >= 0:
                if board[row][col] == 'Q':
                    return False
                col -= 1

            row, col = tempRow, tempCol

            # Check in all the lower diagonal positions (negative slope diagonal)
            while row < n and col >= 0:
                if board[row][col] == 'Q':
                    return False
                row, col = row+1, col-1
            
            return True

        solve(0)

        return res