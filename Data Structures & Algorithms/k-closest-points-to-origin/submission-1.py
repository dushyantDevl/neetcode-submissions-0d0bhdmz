class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            distanceFromOrigin = x**2 + y**2
            minHeap.append([distanceFromOrigin, x, y])

        heapq.heapify(minHeap)
        res = []
        while k:
            _, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1

        return res