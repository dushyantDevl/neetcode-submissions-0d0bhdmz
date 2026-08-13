class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if not self.leftMaxHeap:
            heapq.heappush(self.leftMaxHeap, -num)
        else:
            if num > (-self.leftMaxHeap[0]):
                heapq.heappush(self.rightMinHeap, num)
            else:
                heapq.heappush(self.leftMaxHeap, -num)

            # Balance Heaps
            ## Make sure size of rightMinHeap shouldn't be greater than 
            ## leftMaxHeap bcoz median will be either top of leftMaxHeap 
            ## (in case of odd length) or the average of top elements from both
            ## leftMaxHeap & rightMinHeap (when both heaps have same size)
            if len(self.rightMinHeap) > len(self.leftMaxHeap):
                # put the rightMinHeap top to leftMaxHeap for balancing
                heapq.heappush(self.leftMaxHeap, -heapq.heappop(self.rightMinHeap))
            elif len(self.leftMaxHeap) > len(self.rightMinHeap)+1:
                ## leftMaxHeap also shouldn't have more than rightMinHeap+1 
                ## elements e.g. len(leftMaxHeap)=6 and len(rightMinHeap)=4
                ## isn't allowed (to keep the balance)
                heapq.heappush(self.rightMinHeap, -heapq.heappop(self.leftMaxHeap))

            

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            return -self.leftMaxHeap[0]
        else:
            return ((-self.leftMaxHeap[0]) + self.rightMinHeap[0]) / 2