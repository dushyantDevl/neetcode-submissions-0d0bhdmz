class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n, res = len(arr), []
        for i in range(n):
            rightGreatest = 0
            for j in range(i+1, n):
                if arr[j] > rightGreatest:
                    rightGreatest = arr[j]
            res.append(rightGreatest)
        res[n-1] = -1
        return res