class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                temp.append(matrix[i][j])
        l, r = 0, len(temp)-1
        while l <= r:
            mid = (l+r)//2
            if temp[mid] == target: return True
            elif temp[mid] > target: r = mid-1
            else: l = mid+1
        return False