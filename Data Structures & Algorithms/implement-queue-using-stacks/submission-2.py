class MyQueue:

    def __init__(self):
        self.ip = []
        self.op = []

    def push(self, x: int) -> None:
        self.ip.append(x)

    def pop(self) -> int:
        if self.op:
            return self.op.pop()
        else:
            while self.ip:
                self.op.append(self.ip.pop())
            return self.op.pop()

    def peek(self) -> int:
        if self.op:
            return self.op[-1]
        else:
            while self.ip:
                self.op.append(self.ip.pop())
            return self.op[-1]

    def empty(self) -> bool:
        return not self.ip and not self.op


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()