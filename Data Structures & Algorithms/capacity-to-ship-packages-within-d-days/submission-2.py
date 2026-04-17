class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minWeight = maxWeight = 0
        for weight in weights:
            minWeight = max(minWeight, weight)
            maxWeight += weight

        minCap = minWeight

        def canShip(weight: int):
            currWeight, currDay = weight, 1
            for w in weights:
                if currWeight - w < 0:
                    currDay += 1
                    if currDay > days:
                        return False
                    currWeight = weight
                currWeight -= w
            return True

        while minWeight <= maxWeight:
            midWeight = minWeight + (maxWeight-minWeight)//2
            if canShip(midWeight):
                maxWeight = midWeight-1
                minCap = midWeight
            else:
                minWeight = midWeight + 1
        
        return minCap


