class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topRow, bottomRow = 0, len(matrix)-1
        
        while topRow <= bottomRow:
            reqRow = (topRow + bottomRow) // 2
            if target > matrix[reqRow][-1]: topRow = reqRow + 1
            elif target < matrix[reqRow][0]: bottomRow = reqRow - 1
            else:
                if target == matrix[reqRow][-1] or target == matrix[reqRow][0]: return True
                else: break
        
        if not (topRow <= bottomRow): return False

        reqRow, l, r = (topRow + bottomRow) // 2, 0, len(matrix[0])-1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[reqRow][m]: return True
            elif target > matrix[reqRow][m]: l = m + 1
            else: r = m - 1
        
        return False
