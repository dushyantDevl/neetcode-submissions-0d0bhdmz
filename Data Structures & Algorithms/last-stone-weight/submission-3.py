class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            netWeight = heapq.heappop(maxHeap)-heapq.heappop(maxHeap)
            if netWeight:
                heapq.heappush(maxHeap, netWeight)
        return -maxHeap[0] if maxHeap else 0