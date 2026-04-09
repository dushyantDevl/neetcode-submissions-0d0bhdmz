class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c != "]": stk.append(c)
            else:
                sub_s = ""
                while stk[-1] != "[":
                    sub_s = stk.pop() + sub_s
                stk.pop() # pop "["

                k = ""
                while stk and stk[-1].isdigit(): 
                    k = stk.pop() + k
                stk.append(int(k) * sub_s)

        return "".join(stk)