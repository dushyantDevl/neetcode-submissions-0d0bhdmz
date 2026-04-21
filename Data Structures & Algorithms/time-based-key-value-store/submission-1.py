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
        if key in self.data:
            for i in range(len(self.data[key])-1, -1, -1):
                if timestamp >= self.data[key][i][1]:
                    return self.data[key][i][0]
        return ""
