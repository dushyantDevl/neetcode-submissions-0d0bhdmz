class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for b in s:
            if b=='(' or b=='{' or b=='[':
                stk.append(b)
            else:
                if stk:
                    top_bracket = stk[-1]

                    if ((b==')' and top_bracket=='(') or 
                        (b=='}' and top_bracket=='{') or 
                        (b==']' and top_bracket=='[')):
                        stk.pop()
                    else:
                        return False
                else:
                    return False
        return True if not stk else False
