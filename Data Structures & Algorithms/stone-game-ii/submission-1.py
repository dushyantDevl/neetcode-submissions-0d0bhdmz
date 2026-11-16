class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        ## dp[isAlice][idx][M] = max stones Alice can collect from piles[idx:],
        ## given it's isAlice's turn and the current value of M
        ## isAlice: 1 = Alice's turn, 0 = Bob's turn
        ## M dimension needs n+1 slots because max(M, x) can reach n
        dp = [[[0] * (n + 2) for _ in range(n + 1)] for _ in range(2)]

        ## Base Case is already baked in: dp[*][n][*] = 0 (idx == n means no piles left,
        ## which is the `if idx >= n: return 0` of the recursion)

        ## idx must go BACKWARDS: dp[.][idx][.] only reads dp[.][idx + x][.] where x >= 1,
        ## i.e. strictly larger idx, so every cell it needs is already filled
        for idx in range(n - 1, -1, -1):
            ## M order doesn't matter at all -- max(M, x) is always read at idx + x, never at idx
            for M in range(1, n + 1):
                alice = -float('inf')
                bob = float('inf')
                stones = 0

                for x in range(1, min(2 * M, n - idx) + 1):
                    stones += piles[idx + x - 1]   # prefix sum of the x piles taken
                    nM = max(M, x)                 # new reach for the opponent

                    # Alice's turn: bank the stones, then hand over to Bob -> maximize
                    alice = max(alice, stones + dp[0][idx + x][nM])
                    # Bob's turn: add nothing, just pick the worst position for Alice -> minimize
                    bob = min(bob, dp[1][idx + x][nM])

                dp[1][idx][M] = alice
                dp[0][idx][M] = bob

        return dp[1][0][1]   # Alice to move, idx = 0, M = 1