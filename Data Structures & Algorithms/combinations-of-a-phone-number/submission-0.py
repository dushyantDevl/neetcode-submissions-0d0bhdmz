class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        numToChar = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(idx, currStr, n):
            if idx >= n or len(currStr) == len(digits): # both are same conditions
                ## no need to append to the copy this time here since this functions will create 
                ## copy of it at every recursive call
                res.append(currStr)
                return
            
            for c in numToChar[digits[idx]]:

                backtrack(idx+1, currStr + c, n)

        if digits:
            backtrack(0, "", len(digits))
            return res
        
        return res
