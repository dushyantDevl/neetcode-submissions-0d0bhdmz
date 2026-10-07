class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)

        # Memoization with shifted indexes
        dp = [[-1]*(word2Len+1) for _ in range(word1Len+1)]

        def memoization(idx_1, idx_2):
            # Base Case
            if idx_1 == 0: # If we've done traversing word1
                ## idx_2 can be at any position, now if we are done traversing
                ## word1 that means there are no characters to compare, so just
                ## insert whatever character left in word2
                # return idx_2+1 # no. of characters left to traverse in word2
                return idx_2 # for 1-based indexing (shifted indexes)
            
            if idx_2 == 0: # If we're done traversing word2
                ## idx_1 can be at any position, now if we are done traversing
                ## word2 that means there are no characters to compare, so just
                ## delete whatever character left in word1, bcoz we've to 
                ## convert word1 (substring of it) to empty string (word2 is 
                ## fully traversed)
                # return idx_1+1 # no. of characters left to traverse in word1
                return idx_1 # for 1-based indexing (shifted indexes)

            # Caching
            if dp[idx_1][idx_2] != -1:
                return dp[idx_1][idx_2]

            if word1[idx_1-1] == word2[idx_2-1]: # characters matched!
                ## Since characters are same at these indexes, we don't have to
                ## perform any operation, just go to next character
                # return 0 + memoization(idx_1-1, idx_2-1)
                dp[idx_1][idx_2] = 0 + memoization(idx_1-1, idx_2-1)
                return dp[idx_1][idx_2]

            # Now we've 3 options to edit word1 (since these are the 
            # characters not matching case), explore all of those and 
            # return minimum no. of operation

            ## insert the same character which is at idx_2 of word2 to word1
            ## now, that the character at idx_2 of word2 is matched with that
            ## newly inserted character, we've to go look for other remaining
            ## characters in word2 (that's why idx_2-1) and since we can still
            ## find matching character on word1 at idx_1 from the remaining
            ## characters in word2, idx_1 will stay at same position
            insertion = 1 + memoization(idx_1,idx_2-1)

            ## delete a character from word1, so we've to move to the next
            ## character in word1 (that's why idx_1-1) but since we've not found
            ## a match for a character at idx_2 of word2, idx_2 will stay same
            deletion = 1 + memoization(idx_1-1,idx_2)

            ## We obviously going to replace the same character as word2[idx_2]
            ## on word1 at idx_1, therfore we can just count this as one 
            ## operation and move to next characters from both string 
            ## for comparison of the remaining ones 
            replaced = 1 + memoization(idx_1-1, idx_2-1)

            
            # return min(insertion, deletion, replaced)
            dp[idx_1][idx_2] = min(insertion, deletion, replaced)
            return dp[idx_1][idx_2]

        return memoization(word1Len, word2Len)