class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dictSet = set(wordDict)
        # to not check for substring of length more than the max length word in wordDict
        maxLen = max([len(w) for w in wordDict])

        ## cache list will store true for substring of s of length from 0 to n if they can
        ## be space separated by words in wordDict
        cache = [False] * (n+1)
        # Base Case
        cache[0] = True # for empty string we can decide to not take any word from wordDict

        for i in range(1, n+1):
            # Check for prefixes upto maxLen length
            for j in range(i-1, max(-1,i-maxLen-1), -1):
                # if the substring from 0 to j can be space separated and
                if cache[j] and s[j:i] in dictSet:
                    cache[i] = True
                    break
        
        return cache[n]