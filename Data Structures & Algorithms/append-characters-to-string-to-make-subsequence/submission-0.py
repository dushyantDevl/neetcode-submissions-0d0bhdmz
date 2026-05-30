class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for c in s:
            if i < len(t) and t[i] == c:
                i += 1
        return len(t) - i