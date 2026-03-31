class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for operation in operations:
            if operation == "+":
                stk.append(stk[-2] + stk[-1])
            elif operation == "D":
                stk.append(stk[-1] * 2)
            elif operation == "C":
                stk.pop()
            else:
                stk.append(int(operation))
        return sum(stk)