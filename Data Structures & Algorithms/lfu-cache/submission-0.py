class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: [value, frequency, timestamp]}
        self.timestamp = 0


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.timestamp += 1
        self.cache[key][1] += 1
        self.cache[key][2] = self.timestamp
        
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        self.timestamp += 1
        if key in self.cache:
            self.cache[key][0] = value
            self.cache[key][1] += 1
            self.cache[key][2] = self.timestamp
            return

        if self.capacity <= len(self.cache): 
            minFreq = minTimestamp = float('inf')
            leastFreqKey = -1
            for k,(_,freq,ts) in self.cache.items():
                if minFreq > freq or (minFreq == freq and ts < minTimestamp):
                    minFreq = freq
                    minTimestamp = ts
                    leastFreqKey = k
            
            if leastFreqKey != -1:
                del self.cache[leastFreqKey]

        # Also take care of the case when key doesn't exist but there is space available for storing in cache
        self.cache[key] = [value, 1, self.timestamp]

        
            



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)