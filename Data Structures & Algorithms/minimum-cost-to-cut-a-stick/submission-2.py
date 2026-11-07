class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # To apply the partition DP method i.e. to solve both left and right partitions separately we've to sort
        # the `cuts` list so that indexes use to divide the stick not get mixed either of partitions bcoz we do 
        # need the length of the current piece containing that position
        cuts.sort()

        # Since initial length of stick will be `n`, so to just make the future calculations easy, add `0` at start
        # and `n` at end (`cuts` will still stays as sorted)
        cuts = [0] + cuts + [n]

        m = len(cuts) - 2  # Number of actual cut points

        # Tabulation (Bottom-Up)
        # Size dp array to (m + 2) x (m + 2) to safely handle base cases like dp[k+1][j]
        dp = [[0] * (m + 2) for _ in range(m + 2)]

        for i in range(n,0,-1):
            for j in range(i,m+1): # Base case covered here
                res = float('inf')
                for k in range(i,j+1):
                    # `cuts[j+1] - cuts[i-1]` is the length of current piece, then finding for remaining pieces
                    cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                    res = min(res, cost)

                dp[i][j] = res

        
        return dp[1][m]