class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [-1]*n
        rightGreatest = -1
        for i in range(n-1,-1,-1):
            res[i] = rightGreatest
            rightGreatest = rightGreatest if rightGreatest > arr[i] else arr[i]
        return res