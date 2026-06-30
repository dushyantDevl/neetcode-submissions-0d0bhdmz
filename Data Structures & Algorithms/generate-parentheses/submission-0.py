class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open paranthesis if open < n
        # Only add a closing paranthesis if closed < open
        # Valid (append in res) Iff open == closed == n

        res, stk = [], []

        def backtrack(openParenthesis, closedParenthesis):
            if openParenthesis == closedParenthesis == n:
                res.append("".join(stk))
                return

            if openParenthesis < n:
                stk.append("(")
                backtrack(openParenthesis + 1, closedParenthesis)
                stk.pop()
            
            if closedParenthesis < openParenthesis:
                stk.append(")")
                backtrack(openParenthesis, closedParenthesis + 1)
                stk.pop()

        backtrack(0, 0)
        return res