class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        # whenever '*' appears in string we've to consider as whole WITH its PREVIOUS CHARACTER, just a single '*'
        # without any character before it doesn't mean anything
        ## e.g. while comparing "nnn" vs "n*" character by character, for 2nd string keep the pointer at 'n' and
        ## then check for all the cases we can make by using 0 character or 'n' as many times as require, not
        ## including means ignoring all of 'n*'
        ## e.g. in case of '.*' string we can use any character as many times as require

        dp = [[-1]*(len_p+1) for _ in range(len_s+1)]

        def memoization(idx_s, idx_p):
            # Base Case
            if idx_p == len_p:
                return idx_s == len_s

            if dp[idx_s][idx_p] != -1:
                return dp[idx_s][idx_p]

            charsMatched = False
            if idx_s < len_s and (p[idx_p]==s[idx_s] or p[idx_p]=='.'):
                charsMatched = True

            # two choices in case when pattern has '*' character
            if idx_p + 1 < len_p and p[idx_p + 1] == '*': # starting from 1 bcoz '*' always comes after a character (or '.')
                # compare with remaining pattern if choose to ignore '*'
                notTake = memoization(idx_s, idx_p + 2)
                take = charsMatched and memoization(idx_s + 1, idx_p)

                dp[idx_s][idx_p] = notTake or take
                return dp[idx_s][idx_p]

            # when there's no '*' character we just have to compare character by character (or '.' with any)
            dp[idx_s][idx_p] = charsMatched and memoization(idx_s + 1, idx_p + 1)
            return dp[idx_s][idx_p]

        return memoization(0, 0)
