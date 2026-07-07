class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res, word = [], []

        def backtrack(idx, n):
            if idx == n:
                res.append(" ".join(word))
                return

            for i in range(idx, n):
                w = s[idx:i+1]
                if w in wordDict:
                    word.append(w)
                    backtrack(i+1, n)
                    word.pop()

        backtrack(0, len(s))
        return res