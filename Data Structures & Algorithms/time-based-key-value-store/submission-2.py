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
        res = ""
        if key in self.data:
            l, r = 0, len(self.data[key])-1
            while l <= r:
                m = (l+r)//2
                if self.data[key][m][1] <= timestamp:
                    res = self.data[key][m][0]
                    l = m+1
                else:
                    r = m-1     
        return res