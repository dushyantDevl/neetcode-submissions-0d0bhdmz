class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Len, s2Len, s3Len = len(s1), len(s2), len(s3)
        if s1Len + s2Len != s3Len:
            return False

        dp = {}

        def memoization(i1, i2):
            # Finished traversing both s1 & s2 that means we've formed s3 so return True
            if i1 + i2 == s3Len:
                return True

            if (i1,i2) in dp:
                return dp[(i1,i2)]

            ## explore both possibilities in case if character at i1 & i2 from s1 & s2 respectively are same as on 
            ## `s3[i1+i2]`. for e.g. if character at i1=2(on s1) and i2=3(on s2) is same as on i3=5 (on s3) then explore
            ## or traverse all remaining indexes from both strings s1 and s2 if any one of them forms s3

            ## Directly return True if any one path leads to it without any caching
            if i1 < s1Len and s1[i1] == s3[i1+i2] and memoization(i1+1, i2):
                return True
            if i2 < s2Len and s2[i2] == s3[i1+i2] and memoization(i1, i2+1):
                return True

            dp[(i1,i2)] = False
            return False

        return memoization(0,0)