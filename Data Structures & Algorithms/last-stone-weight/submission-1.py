class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        maxHeap = []
        for stoneWeight in stones:
            heapq.heappush(maxHeap, -stoneWeight)
        
        while len(maxHeap) > 1:
            heavyStone1, heavyStone2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if heavyStone1 > heavyStone2:
                maxHeap.append(heavyStone1 - heavyStone2)
            elif heavyStone1 < heavyStone2:
                maxHeap.append(heavyStone2 - heavyStone1)
        
        return maxHeap[0] if maxHeap else 0


        