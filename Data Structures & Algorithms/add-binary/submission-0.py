class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        res, carry = "", 0

        a, b = a[::-1], b[::-1]
        for i in range(max(len_a, len_b)):
            digitA = ord(a[i]) - ord("0") if i < len_a else 0
            digitB = ord(b[i]) - ord("0") if i < len_b else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res

        return res