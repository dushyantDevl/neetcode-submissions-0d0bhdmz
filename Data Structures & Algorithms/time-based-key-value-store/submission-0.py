class TimeMap:

    def __init__(self):
        self.data = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.append((timestamp, key, value))
        self.data.sort(key=lambda x:x[0])

    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.data)-1,-1,-1):
            if self.data[i][0] <= timestamp and self.data[i][1] == key:
                return self.data[i][2]
        return ""