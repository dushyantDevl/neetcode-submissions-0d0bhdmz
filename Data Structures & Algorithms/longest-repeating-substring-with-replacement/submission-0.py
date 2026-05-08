class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # To check this, we track the most frequent character inside the substring — everything 
        # else would need to be replaced. If the number of replacements needed is within k, we 
        # update the answer.
        i, maxLen, charF, maxF = 0, 0, [0]*26, 0
        for j in range(len(s)):
            charF[ord(s[j]) - ord('A')] += 1
            maxF = max(maxF, max(charF))
            # check to see if characters can replace k or less characters (other than most frequent character)
            if j-i+1 - maxF <= k: # current window size - max frequent character
                maxLen = max(maxLen, j-i+1)
            else: # no longer replace the characters with most frequent one
                charF[ord(s[i]) - ord('A')] -= 1 # update the character count after shrinking
                i += 1 # shrink the window
        return maxLen

