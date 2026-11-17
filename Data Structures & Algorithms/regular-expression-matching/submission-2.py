class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # whenever '*' appears in string we've to consider as whole WITH its PREVIOUS CHARACTER, just a single '*'
        # without any character before it doesn't mean anything
        ## e.g. while comparing "nnn" vs "n*" character by character, for 2nd string keep the pointer at 'n' and
        ## then check for all the cases we can make by using 0 character or 'n' as many times as require, not
        ## including means ignoring all of 'n*'
        ## e.g. in case of '.*' string we can use any character as many times as require

        # Base Case
        if len(p) == 0:
            return len(s) == 0

        charsMatched = False
        if len(s) > 0 and (s[0]==p[0] or p[0]=='.'):
            charsMatched = True

        # two choices in case when pattern has '*' character
        if len(p) > 1 and p[1] == '*': # starting from 1 bcoz '*' always comes after a character (or '.')
            # compare with remaining pattern if choose to ignore '*'
            notTake = self.isMatch(s, p[2:])
            take = charsMatched and self.isMatch(s[1:], p)

            return notTake or take

        # when there's no '*' character we just have to compare character by character (or '.' with any)
        return charsMatched and self.isMatch(s[1:], p[1:])
