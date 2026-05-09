class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        
        charCount1, charCount2 = [0]*26, [0]*26
        
        for i in range(n1):
            charCount1[ord(s1[i])-ord('a')] += 1
            charCount2[ord(s2[i])-ord('a')] += 1
        
        if charCount1 == charCount2: return True

        l = 0
        for r in range(n1, n2):
            charCount2[ord(s2[r])-ord('a')] += 1
            charCount2[ord(s2[l])-ord('a')] -= 1
            l += 1
            if charCount1 == charCount2: return True
        
        return False

        