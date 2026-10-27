class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        
        ## since it just asks for sequence not subsequence we can change the order of strings and just look for subset
        ## instead, sorting by length will be helpful while traversing the `words` list bcoz string at current index 
        ## will always going to have greater length then all the strings at previous indexes
        words = sorted(words, key=lambda x:len(x))
        
        ## This problem is just a extension of Longest Increasing Subsequence with difference being we've to look for 
        ## longest string chain instead of increasing subsequence, so the code will be similar too just check for chain
        ## here instead of checking increasing sequence
        dp = [1]*n

        def isChain(s1, s2):
            lenS1, lenS2 = len(s1), len(s2)
            
            ## s2 string represent the current string whereas s1 is for previous strings that's why current string's
            ## length will always be greater (bcoz we sorted length wise)
            if lenS2 != lenS1 + 1:
                return False
            i1 = i2 = 0
            while i2 < lenS2:
                if i1 < lenS1 and s1[i1] == s2[i2]:
                    i1 += 1
                    i2 += 1
                else:
                    i2 += 1

            ## return True iff both pointer finished traversing at the same time, bcoz we increment i2 only and not i1
            ## when characters are different, the loop will take care of one extra character and i1 & i2 will finished
            ## traversing at the same moment
            if i1 == lenS1 and i2 == lenS2:
                return True

            return False

        res = 1
        for idx in range(n):
            for prevIdx in range(idx):
                if isChain(words[prevIdx], words[idx]) and 1+dp[prevIdx] > dp[idx]:
                    dp[idx] = 1 + dp[prevIdx]
            res = max(res, dp[idx])


        return res