class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ## cache will stores cost to reach at certain index `i` initializing all elements with 0
        ## will help in putting 0 cost on 0th and 1st step (since we can start from either)
        cache = [0] * (n+1)

        for i in range(2, n+1):
            oneStep = cost[i-1] + cache[i-1]
            twoStep = cost[i-2] + cache[i-2]
            
            cache[i] = min(oneStep, twoStep)

        return cache[n]