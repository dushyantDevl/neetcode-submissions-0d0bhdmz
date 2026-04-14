class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start_x, start_y = 0, cols-1
        while start_x < rows and start_y >=0:
            if matrix[start_x][start_y] == target: return True
            elif matrix[start_x][start_y] > target: start_y -= 1
            else: start_x += 1
        return False