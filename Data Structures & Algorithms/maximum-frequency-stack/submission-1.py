class FreqStack:

    def __init__(self):
        self.stk = []
        self.freqMap = {}

    def push(self, val: int) -> None:
        self.freqMap[val] = self.freqMap.get(val, 1) + 1
        self.stk.append((val, self.freqMap[val]))

    def pop(self) -> int:
        maxFreq = 0
        for num_freq in self.stk:
            if num_freq[1] > maxFreq:
                maxFreq = num_freq[1]
        
        for i in range(len(self.stk)-1, -1, -1):
            if self.stk[i][1] == maxFreq:
                self.freqMap[self.stk[i][0]] -= 1
                return self.stk.pop(i)[0]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()