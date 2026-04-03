class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == '+':
                a = stk.pop()
                b = stk.pop()
                stk.append(b+a)
            elif token == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif token == '*':
                a = stk.pop()
                b = stk.pop()
                stk.append(b*a)
            elif token == '/':
                a = stk.pop()
                b = stk.pop()
                # stk.append(b//a) # since it's a floor division it'll give smaller negative integer as output in case of negative numbers in decimal
                stk.append(int(b/a)) # int(b/a) will just chop off everything after decimal
            else:
                stk.append(int(token))
        return stk[-1]
