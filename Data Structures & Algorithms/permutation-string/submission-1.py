class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        charCount1 = {}
        for c in s1:
            charCount1[c] = charCount1.get(c, 0) + 1
        
        # charNeed represent unique characters in s1
        charNeed = len(charCount1)

        for i in range(n2):
            charCount2 = {}
            noOfcurrChar = 0 # number of character at current iteration that were in s1
            for j in range(i, n2):
                charCount2[s2[j]] = charCount2.get(s2[j], 0) + 1
                # if char count in charCount2 has already exceed what's in s1 then no need to check further
                if charCount2[s2[j]] > charCount1.get(s2[j], 0):
                    break
                if charCount1.get(s2[j], 0) == charCount2[s2[j]]:
                    noOfcurrChar += 1
                if noOfcurrChar == charNeed: # already checked frequency in previous step now just check the length of substring
                    return True

        return False
        