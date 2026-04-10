class FreqStack:

    def __init__(self):
        self.stk = []
        self.freqMap = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqMap[val] += 1
        self.stk.append(val)

    def pop(self) -> int:
        maxFreq = max(self.freqMap.values())
        i = len(self.stk)-1
        while self.freqMap[self.stk[i]] != maxFreq: i -= 1
        self.freqMap[self.stk[i]] -= 1
        return self.stk.pop(i)

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()