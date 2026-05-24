class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if not key in self.cache: 
            return -1
        
        res = self.cache[key]
        del self.cache[key]
        self.cache[key] = res # put the key-value pair again for marking it as most recent used (last position in hash)
        return res

    def put(self, key: int, value: int) -> None:
        # Update value if key already exists
        if key in self.cache:
            # If it exists, delete it so we can re-insert at the end with new value
            del self.cache[key]
        # When key doesn't exists and capacity is full
        elif len(self.cache) == self.capacity:
            leastRecentlyUsedKey = next(iter(self.cache))
            del self.cache[leastRecentlyUsedKey] # remove the 
        
        # insert or update the key (goes to last position automatically)
        self.cache[key] = value
