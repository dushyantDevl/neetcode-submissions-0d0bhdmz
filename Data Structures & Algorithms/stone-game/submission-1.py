class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # Check for each two choices for Alice at each step since Bob score will be just total sum minus Alice score
        dp = {}

        def memoization(l, r): # returns Max Alice total
            if l > r: # No elements to choose from
                return 0

            if (l,r) in dp:
                return dp[(l,r)]
            
            # if even no. of stones remaining -> Alice is choosing the pile if not then it's Bob
            even = (r-l) % 2 == 0
            # Since we're only considering Alice choices here, return 0 when Alice isn't picking any piles
            left = piles[l] if even else 0 # Alice can pick from left side iff remaining `piles` length is even
            right = piles[r] if even else 0 # Alice can pick from right side iff remaining `piles` length is even

            dp[(l,r)] = max(
                        # Alice picks from left, so remaining subarray for Bob will be from l+1 to r
                        memoization(l+1, r) + left,
                        # Alice picks from right, so remaining subarray for Bob will be from l to r-1
                        memoization(l, r-1) + right
            )

            return dp[(l,r)]

        return memoization(0, n-1) > (sum(piles)//2) # one who scores more than half, wins

            

