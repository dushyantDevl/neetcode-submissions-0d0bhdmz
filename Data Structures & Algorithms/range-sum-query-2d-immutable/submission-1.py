class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROW, COL = len(self.matrix), len(self.matrix[0])
        self.prefixRowWiseSum = []

        for r in range(ROW):
            temp = [self.matrix[r][0]]
            for c in range(1,COL):
                temp.append(temp[c-1]+self.matrix[r][c])
            self.prefixRowWiseSum.append(temp)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        regionSum = 0
        for i in range(row1, row2+1):
            if col1>0:
                regionSum += self.prefixRowWiseSum[i][col2]-self.prefixRowWiseSum[i][col1-1]
            else:
                regionSum += self.prefixRowWiseSum[i][col2]

        return regionSum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)