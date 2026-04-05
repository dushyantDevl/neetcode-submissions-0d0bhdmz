class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        span = 1
        for i in range(len(self.arr)-2, -1, -1):
            if price >= self.arr[i]:
                span += 1 
            else:
                break
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)