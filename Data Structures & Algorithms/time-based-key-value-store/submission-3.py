import bisect

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((value, timestamp))
        else:
            self.data[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        values = self.data[key]
        # Use bisect_right to find the point AFTER our target
        idx = bisect.bisect_right(values, timestamp, key=lambda x: x[1])
        
        # If idx is 0, it means the smallest timestamp in our list is 
        # already bigger than the requested 'timestamp'.
        if idx == 0: return ""
        
        # Subtract 1 to get the largest timestamp <= target
        return values[idx - 1][0]