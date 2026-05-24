class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ds = []
        self.timeStamp = 0

    def get(self, key: int) -> int:
        for i in range(len(self.ds)):
            if self.ds[i][0] == key:
                self.timeStamp += 1
                self.ds[i][2] = self.timeStamp
                return self.ds[i][1]
        return -1

    def put(self, key: int, value: int) -> None:
        # Update value if key already exists
        for i in range(len(self.ds)):
            if self.ds[i][0] == key:
                self.ds[i][1] = value
                self.timeStamp += 1
                self.ds[i][2] = self.timeStamp
                return

        # When key doesn't exists and capacity is full
        if len(self.ds) == self.capacity:
            leastUsed, delIdx = float('inf'), -1
            for i in range(len(self.ds)):
                if self.ds[i][2] < leastUsed:
                    leastUsed = self.ds[i][2]
                    delIdx = i
            del self.ds[delIdx]
            self.timeStamp += 1
            self.ds.append([key, value, self.timeStamp])
        else: # When capacity isn't full
            self.timeStamp += 1
            self.ds.append([key, value, self.timeStamp])
