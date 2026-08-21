class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # T.C => O(NlogN)
        trips.sort(key = lambda trip: trip[1]) # to keep track of which trip starts first

        currPassengers = 0
        
        # Find the smallest trip that will ends first to know which passengers will drop first
        minHeap = [] # [[endPos, numPassengers]]

        # T.C => O(NlogN)
        for trip in trips:
            numPassengers, startPos, endPos = trip

            ## update currPassengers if some trip has ended by reducing the currPassengers by
            ## no. of passengers whose trip has ended and also pop from minHeap since its not
            ## needed anymore
            while minHeap and minHeap[0][0] <= startPos:
                currPassengers -= heapq.heappop(minHeap)[1]

            currPassengers += numPassengers
            if currPassengers > capacity:
                return False

            ## push the ongoing trips, if current trip isn't possible, above condition will
            ## return False 
            heapq.heappush(minHeap, [endPos, numPassengers])

        return True