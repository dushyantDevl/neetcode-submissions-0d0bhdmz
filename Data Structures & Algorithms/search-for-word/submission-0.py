class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nRows, nCols = len(board), len(board[0])
        path = set()

        def backtrack(row, col, idx):
            if idx == len(word): # reached to last character of the word
                return True

            # Invalid moves
            if (    
                    row < 0 or col < 0 or # invalid index
                    row >= nRows or col >= nCols or # invalid index
                    word[idx] != board[row][col] or # current char on board is different
                    (row, col) in path # already visited
                ):
                return False

            # Valid moves
            path.add((row, col))
            # visit to each cell in all four direction (if possible)
            res = (
                    backtrack(row+1, col, idx+1) or
                    backtrack(row-1, col, idx+1) or
                    backtrack(row, col+1, idx+1) or
                    backtrack(row, col-1, idx+1)
                )

            # remove the cell when going back to previous function call (i.e. backtracking)
            path.remove((row, col))

            return res


        for r in range(nRows):
            for c in range(nCols):
                # only run if the first character of word and char at start of path are same
                # if word[0] == board[r][c]:
                if backtrack(r, c, 0):
                    return True

        return False
