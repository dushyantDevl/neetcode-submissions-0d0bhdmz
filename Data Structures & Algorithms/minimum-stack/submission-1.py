class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        if not self.stk:
            self.minStk.append(val)
        elif self.minStk[-1] >= val:
            self.minStk.append(val)
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.minStk[-1]:
            self.minStk.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.minStk[-1]
