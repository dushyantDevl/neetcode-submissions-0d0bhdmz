class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1,y1,x2,y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)

        # Store distance from origin and idx of the point from points
        distFromOrigin = [(distance(x[0],x[1],0,0),i) for i,x in enumerate(points)]
        # distance will get the priority by default so lower distance will have more priority
        heapq.heapify(distFromOrigin) # min heap by default
        
        res = []
        
        while k:
            point = heapq.heappop(distFromOrigin)
            res.append(points[point[1]])
            k -= 1
        return res

        