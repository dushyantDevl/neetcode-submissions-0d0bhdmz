class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap by negating all stone weights
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # Pop two heaviest stones (remember to negate back)
            heavyStone1 = -heapq.heappop(maxHeap)
            heavyStone2 = -heapq.heappop(maxHeap)

            # If they are not equal, push the difference back (negated)
            if heavyStone1 != heavyStone2:
                heapq.heappush(maxHeap, -(heavyStone1 - heavyStone2))

        # Return the last remaining stone or 0 if none left
        return -maxHeap[0] if maxHeap else 0