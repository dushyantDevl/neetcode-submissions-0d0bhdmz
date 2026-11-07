from functools import cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # To apply the partition DP method i.e. to solve both left and right partitions separately we've to sort
        # the `cuts` list so that indexes use to divide the stick not get mixed either of partitions bcoz we do 
        # need the length of the current piece containing that position
        cuts.sort()

        # Since initial length of stick will be `n`, so to just make the future calculations easy, add `0` at start
        # and `n` at end (`cuts` will still stays as sorted)
        cuts = [0] + cuts + [n]

        @cache
        def memoization(i, j):
            if i > j:
                return 0

            res = float('inf')

            for k in range(i,j+1):
                # `cuts[j+1] - cuts[i-1]` is the length of current piece, then finding for remaining pieces
                cost = cuts[j+1] - cuts[i-1] + memoization(i,k-1) + memoization(k+1,j)
                res = min(res, cost)

            return res

        # Actual cut positions are from index 1 to len(cuts) - 2
        return memoization(1, len(cuts) - 2)