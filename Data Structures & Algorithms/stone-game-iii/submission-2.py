class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # Tabulation (Space Optimized)
        curr = nxt = nxt2nxt = 0

        for idx in range(n-1,-1,-1):
            # Alice/Bob takes one pile then call recursion for rest, subtract the next score
            res = stoneValue[idx] - curr
            
            # Both plays optimally so maximize the score everytime, no matter who's turn it is and since both have
            # same no. of choices at any time, we don't have to make separate call for each score, which makes it
            # to directly calculate score difference
            if idx+1 < n:
                # Alice/Bob takes two pile then call recursion for rest, subtract the next score
                res = max(res, stoneValue[idx] + stoneValue[idx+1] - nxt)
            if idx+2 < n:
                # Alice/Bob takes three pile then call recursion for rest, subtract the next score
                res = max(res, stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2] - nxt2nxt)

            nxt2nxt = nxt
            nxt = curr
            curr = res

        if curr > 0:
            return "Alice"
        elif curr < 0:
            return "Bob"

        return "Tie"