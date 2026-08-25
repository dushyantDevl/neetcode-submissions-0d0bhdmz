class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def helper(idx):
            if idx < 2:
                return cost[idx] 
            return cost[idx] + min(helper(idx-1), helper(idx-2))

        return min(helper(n-1), helper(n-2)) # top reachable from either