class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        for i in range(len(trips)):
            current_required_capacity = trips[i][0]
            for j in range(i):
                if trips[j][2] > trips[i][1]: # Trips which aren't end yet
                    current_required_capacity += trips[j][0]
            if current_required_capacity > capacity:
                return False
        return True