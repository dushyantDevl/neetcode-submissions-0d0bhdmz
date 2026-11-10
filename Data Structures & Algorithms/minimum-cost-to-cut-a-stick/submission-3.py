class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # If we try every permutation of `cuts`, this will end up around n! time complexity

        dp = {} # caching

        def memoization(l, r):
            if r-l == 1: # can't cut the stick any further
                return 0

            if (l,r) in dp:
                return dp[(l,r)]

            res = float('inf')

            for c in cuts:
                if l < c < r:
                    res = min(
                        res,
                        # length of current stick + cut in left partition + cut in right partition
                        (r-l) + memoization(l,c) + memoization(c,r)
                    )
            
            dp[(l,r)] = 0 if res == float('inf') else res
            return dp[(l,r)]

        return memoization(0,n)