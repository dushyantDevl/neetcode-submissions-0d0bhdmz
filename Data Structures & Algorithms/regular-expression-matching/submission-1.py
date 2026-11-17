class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # whenever '*' appears in string we've to consider as whole WITH its PREVIOUS CHARACTER, just a single '*'
        # without any character before it doesn't mean anything
        ## e.g. while comparing "nnn" vs "n*" character by character, for 2nd string keep the pointer at 'n' and
        ## then check for all the cases we can make by using 0 character or 'n' as many times as require, not
        ## including means ignoring all of 'n*'
        ## e.g. in case of '.*' string we can use any character as many times as require

        dp = {}

        def memoization(string, pattern):
            # Base Case
            if len(pattern) == 0:
                return len(string) == 0

            if (string,pattern) in dp:
                return dp[(string,pattern)]

            charsMatched = False
            if len(string) > 0 and (string[0]==pattern[0] or pattern[0]=='.'):
                charsMatched = True

            # two choices in case when pattern has '*' character
            if len(pattern) > 1 and pattern[1] == '*': # starting from 1 bcoz '*' always comes after a character (or '.')
                # compare with remaining pattern if choose to ignore '*'
                notTake = memoization(string, pattern[2:])
                take = charsMatched and memoization(string[1:], pattern)

                dp[(string,pattern)] = notTake or take
                return dp[(string,pattern)]

            # when there's no '*' character we just have to compare character by character (or '.' with any)
            dp[(string,pattern)] = charsMatched and memoization(string[1:], pattern[1:])
            return dp[(string,pattern)]

        return memoization(s, p)
