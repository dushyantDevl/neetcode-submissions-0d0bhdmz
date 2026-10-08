class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Logic:
        ## for any 6 element list, [a,b,c,d,e,f], according to this question
        ## when all the stones are smashed (two at a time) a single value will
        ## remain, and we've to minimize that value, so for e.g.
        ## pick b & e => [a, b-e, c, d, f]
        ## pick a & c => [a-c, b-e, d, f]
        ## pick a-c & d => [a-c-d, b-e, f]
        ## pick b-e & f => [a-c-d, b-e-f]
        ## pick a-c-d & b-e-f => [a-c-d-(b-e-f)] => (a+e+f) - (b+c+d)
        ## as we can see these are just two subset or partition of the list and 
        ## minimizing this i.e. S1 - S2 = ans & S1 + S2 = Total
        ## ans = Total - 2S2, minimizing this means S2 should be as close to
        ## "Total//2" as possible so that the minimum would be 0
        ## Knapsack based DP
        
        n, Total = len(stones), sum(stones)
        dp = [[0]*(Total//2 + 1) for _ in range(n+1)]

        # Base Case
        for wt in range(stones[0], (Total//2 + 1)):
            dp[0][wt] = stones[0]

        for i in range(n):
            for wt in range(Total//2 + 1):
                pick = 0
                if stones[i] <= wt:
                    pick = stones[i] + dp[i-1][wt-stones[i]]
                notPick = dp[i-1][wt]

                dp[i][wt] = max(pick, notPick)

        return Total - 2*dp[n-1][Total//2]