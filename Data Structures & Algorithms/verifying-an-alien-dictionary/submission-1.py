class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        charToIdx = {c: i for i, c in enumerate(order)}
        for i in range(1, n):
            word1, word2 = words[i-1], words[i]
            word1Len, word2Len = len(word1), len(word2)
            
            # compare the order of two words at a time (if they are at correct place or not)
            for j in range(word1Len):
                ## if word1 has more length even tho the characters were same until the 
                ## length of word2, return False (e.g. neet should come before neetcode)
                if j == word2Len:
                    return False

                if word1[j] != word2[j]:
                    if charToIdx[word1[j]] > charToIdx[word2[j]]:
                        return False
                    
                    ## In lexicographical (dictionary) sorting, only the first differing
                    ## character determines the order of the words. Whatever characters 
                    ## come after that first difference are completely irrelevant, so break!
                    break
        return True