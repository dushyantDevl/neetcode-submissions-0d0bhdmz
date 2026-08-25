class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        
        def helper(idx):
            if idx < 2:
                return cost[idx]
            
            if idx in cache:
                return cache[idx]

            cache[idx] = cost[idx] + min(helper(idx-1), helper(idx-2))
            return cache[idx]

        return min(helper(n-1), helper(n-2)) # top reachable from either