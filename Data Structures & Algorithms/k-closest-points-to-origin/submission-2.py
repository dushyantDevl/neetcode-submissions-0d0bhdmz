class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x,y in points:
            distanceFromOrigin = x**2 + y**2
            distance.append([distanceFromOrigin, x, y])

        distance.sort()
        return [[distance[i][1], distance[i][2]] for i in range(k)]