class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix)-1, len(matrix[0])-1
        l, r = 0, (rows * cols) - 1
        while l <= r:
            m = (l+r)//2
            row = m // cols # bcoz no. of elements in the particular row will always be multiple of total number of columns since that's how many element each row contain
            col = m % cols # return a no. between 0 to cols-1, which will always denote the current column
            if target > matrix[row][col]: l = m+1
            elif target < matrix[row][col]: r = m-1
            else: return True
        return False