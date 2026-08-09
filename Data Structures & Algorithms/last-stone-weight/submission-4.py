class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap) # T.C => O(N) bcoz it already has whole list to heapify
        while len(maxHeap) > 1:
            netWeight = heapq.heappop(maxHeap)-heapq.heappop(maxHeap)
            if netWeight: # push only when net weight isn't zero
                heapq.heappush(maxHeap, netWeight)
        return -maxHeap[0] if maxHeap else 0