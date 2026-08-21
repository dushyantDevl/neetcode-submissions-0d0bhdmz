class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # T.C -> O()

        # initially no. of passenger at each 0 to 1000 position point will be 0
        passengerChange = [0] * 1001

        for trip in trips:
            numPassengers, startPos, endPos = trip
            
            # pick up numPassengers no. of passengers from startPos
            passengerChange[startPos] += numPassengers

            # drop of numPassengers no. of passenger from endPos
            passengerChange[endPos] -= numPassengers

        currPassenger = 0
        for i in range(1001):
            currPassenger += passengerChange[i]

            if currPassenger > capacity:
                return False

        return True