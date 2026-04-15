class Solution:
    def totalHours(self, piles: List[int], rate: int) -> int:
        hrs = 0
        for pile in piles: hrs += math.ceil(pile/rate)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # min and max rate of eating bananas
        minRate = r
        while l <= r:
            m = l + (r-l)//2
            hoursTaken = self.totalHours(piles, m)
            if hoursTaken > h: l = m+1 # should increase the rate, so look in right high
            else: # we've to find min rate, so search in lower half
                minRate = min(minRate, m)
                r = m-1
        return minRate