class Solution:
    def numDecodings(self, s: str) -> int:
        # Top-Down Approach (recursive, from last to first position)
        ## We've to take care of 2 characters at a time while traversing the string
        ## since characters can be represented by either 1 or 2 digit number (1 to 26)
        ## this is similar to how in climb stairs or fibonacci sequence we care about the
        ## last 2 digits
        
        n = len(s)

        cache = {}
        
        ## waysToDecode[i] = waysToDecode[i-1] (if new single digit is valid) +
        ##                   waysToDecode[i-2] (if last 2 digits are valid)
        
        def dp(idx): # no. of ways to decode string of length idx+1
            if idx < 0:
                return 1
            
            if idx in cache:
                return cache[idx]

            if s[idx] == '0':
                cache[idx] = 0
                return 0

            # take digit at current index as single number
            res = dp(idx-1)
            
            # Take current + previous digit as a two-digit number
            ## below method also works in this specific case since both are 2 digits 
            ## but semantically converting to int is better
            # if idx > 0 and "10" <= s[idx-1:idx+1] <= "26":
            if idx > 0 and 10 <= int(s[idx-1:idx+1]) <= 26:
                res += dp(idx-2)

            cache[idx] = res
            return res

        return dp(n-1)