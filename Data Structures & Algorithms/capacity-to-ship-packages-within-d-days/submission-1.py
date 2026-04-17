class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = max(weights)
        while True:
            day, cap = 1, minCap
            
            for w in weights:
                if cap - w < 0:
                    day, cap = day+1, minCap
                cap -= w

            if day <= days: return minCap

            minCap += 1