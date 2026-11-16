class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-1] * n

        def memoization(idx): # returns score differnece, `Alice - Bob`
            if idx >= n:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            # Alice/Bob takes one pile then call recursion for rest, subtract the next score
            res = stoneValue[idx] - memoization(idx+1)
            
            if idx+1 < n:
                # Alice/Bob takes two pile then call recursion for rest, subtract the next score
                res = max(res, stoneValue[idx] + stoneValue[idx+1] - memoization(idx+2))
            if idx+2 < n:
                # Alice/Bob takes three pile then call recursion for rest, subtract the next score
                res = max(res, stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2] - memoization(idx+3))

            dp[idx] = res
            return res

        scoreDiff = memoization(0)

        if scoreDiff > 0:
            return "Alice"
        elif scoreDiff < 0:
            return "Bob"

        return "Tie"