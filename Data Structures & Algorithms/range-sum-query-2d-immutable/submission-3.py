class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preRectSum = [[0]*(COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += self.matrix[r][c]
                above = self.preRectSum[r+1-1][c+1]
                self.preRectSum[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeftSum = self.preRectSum[row1-1+1][col1-1+1]
        topSum = self.preRectSum[row1-1+1][col2+1]
        leftSum = self.preRectSum[row2+1][col1-1+1]
        totalRegionSum = self.preRectSum[row2+1][col2+1]
        return totalRegionSum - topSum - leftSum + topLeftSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)