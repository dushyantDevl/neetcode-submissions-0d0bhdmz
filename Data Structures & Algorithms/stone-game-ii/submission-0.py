class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = {}

        # Game Strategy (for Alice):
        ## When it's your turn, do YOUR BEST (optimal)
        ## When it's your opponent's turn, expect the worst (for optimal result)

        def memoization(isAlice, idx, M): # max stones for Alice, from index=idx 
            # Base Case
            if idx >= n:
                return 0

            if (isAlice, idx, M) in dp:
                return dp[(isAlice, idx, M)]

            res = -float('inf') if isAlice else float('inf')
            stones = 0

            ## Explore all possibilites for Alice i.e. no. of piles she can take at a time, which depends on the value
            ## of M which also depends on how many no. of piles taken by Bob (after its turn) starting from 2 
            ## choices for Alice either taking 0th or 1st index piles then it depends on what piles does Bob chooses
            for x in range(1, min(2*M,n-idx)+1):

                stones += piles[idx + x - 1] # prefix sum of stones for no. of piles Alice can take

                if isAlice:
                    # Add stones taken in result then call the recursion for Bob's turn
                    res = max(res, stones + memoization(False, idx+x, max(M,x)))
                else: # Bob's turn
                    ## since we're only calculating stones for Alice, we don't have to add no. of stones here, bcoz
                    ## this case is for Bob' turn and expecting worst from Bob means take the `min` here
                    res = min(res, memoization(True, idx+x, max(M,x)))
            
            dp[(isAlice, idx, M)] = res
            return res

        return memoization(True, 0, 1)
