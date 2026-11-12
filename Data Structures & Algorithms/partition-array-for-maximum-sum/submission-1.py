class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # Tabulation (Bottom-Top approach) -> call from n-1 to 0
        dp = [0]*(n+1)

        for idx in reversed(range(n)):
            partitionLen, largestVal, res = 0, -2147483647, -2147483647

            for i in range(idx, min(n, idx+k)): # `idx+k` should stay less than length of array
                partitionLen += 1
                largestVal = max(largestVal, arr[i])
                partitionSum = partitionLen * largestVal + dp[i+1]
                res = max(res, partitionSum)

            dp[idx] = res

        return dp[0]