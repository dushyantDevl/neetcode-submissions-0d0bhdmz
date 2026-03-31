class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk, score = [], 0
        for operation in operations:
            if operation == "+":
                score += stk[-2] + stk[-1]
                stk.append(stk[-2] + stk[-1])
            elif operation == "D":
                score += stk[-1] * 2
                stk.append(stk[-1] * 2)
            elif operation == "C":
                score -= stk.pop()
            else:
                score += int(operation)
                stk.append(int(operation))
        return score