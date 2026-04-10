class FreqStack:

    def __init__(self):
        self.freqMap = defaultdict(int)
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.freqMap[val] += 1
        if self.maxCount < self.freqMap[val]:
            self.maxCount = self.freqMap[val]
            self.stacks[self.maxCount] = [] # new frequency -> need new stack
        self.stacks[self.freqMap[val]].append(val) # val in its frequency group

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        self.freqMap[res] -= 1 # decrement of popped element frequency
        if not self.stacks[self.maxCount]: # group with max frequency has no element left
            self.maxCount -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()