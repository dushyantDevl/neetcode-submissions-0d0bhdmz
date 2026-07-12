class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary) # to avoid linear search in list,  make it hashset for O(1) search
        cache = {len(s):0} # memoization

        def dfs(idx):
            # We can skip this base case just by storing this condition in cache itself
            # if idx == len(s): # already checked for all the characters in s
                # return 0 # no character at this position so no extra character too

            if idx in cache:
                return cache[idx]

            ## skip the current character and call dfs for remaining, since we're skipping
            ## a character here that means leaving a extra character
            ## `res` can also be assumed float('inf') or just len(s), since that will be the maximum
            ## character we can skip
            res = 1 + dfs(idx+1) 
            
            ## # check every substring of s to check for every prefix of words in dictionary
            for i in range(idx, len(s)):
                if s[idx:i+1] in words:
                    res = min(res, dfs(i+1))
            cache[idx] = res # save results for memoization
            return res
            
        return dfs(0)