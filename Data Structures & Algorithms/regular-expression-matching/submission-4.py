class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        # whenever '*' appears in string we've to consider as whole WITH its PREVIOUS CHARACTER, just a single '*'
        # without any character before it doesn't mean anything
        ## e.g. while comparing "nnn" vs "n*" character by character, for 2nd string keep the pointer at 'n' and
        ## then check for all the cases we can make by using 0 character or 'n' as many times as require, not
        ## including means ignoring all of 'n*'
        ## e.g. in case of '.*' string we can use any character as many times as require

        # Tabulation (Bottom-Up Approach)
        dp = [[False]*(len_p+1) for _ in range(len_s+1)]

        # Base case: empty string matches empty pattern
        dp[len_s][len_p] = True

        ## The outer loop now starts at len_s instead of len_s - 1. You need to compute the cells in row 
        ## idx_s == len_s (empty string, non-empty pattern) — e.g. "" vs "a*" should be True
        for idx_s in range(len_s, -1, -1):
            for idx_p in range(len_p-1, -1, -1):
                charsMatched = idx_s < len_s and (p[idx_p]==s[idx_s] or p[idx_p]=='.')

                # two choices in case when pattern has '*' character
                if idx_p + 1 < len_p and p[idx_p + 1] == '*': # starting from 1 bcoz '*' always comes after a character (or '.')
                    # compare with remaining pattern if choose to ignore '*'
                    notTake = dp[idx_s][idx_p + 2]
                    take = charsMatched and dp[idx_s + 1][idx_p]

                    dp[idx_s][idx_p] = notTake or take
                else:
                    # when there's no '*' character we just have to compare character by character (or '.' with any)
                    dp[idx_s][idx_p] = charsMatched and dp[idx_s + 1][idx_p + 1]

        return dp[0][0]
