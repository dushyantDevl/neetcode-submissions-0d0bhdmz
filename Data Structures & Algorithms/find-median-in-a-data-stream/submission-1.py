class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()

    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2:
            return self.stream[n//2]
        else:
            return (self.stream[n//2]+self.stream[(n//2)-1]) / 2
        