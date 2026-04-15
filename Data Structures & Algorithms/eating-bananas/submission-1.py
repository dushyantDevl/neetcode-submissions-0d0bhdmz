class Solution:
    def totalHours(self, piles: List[int], rate: int) -> int:
        hrs = 0
        for pile in piles: hrs += math.ceil(pile/rate)
        return hrs

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxRate = max(piles)
        for rate in range(1, maxRate+1):
            if self.totalHours(piles, rate) <= h:
                return rate