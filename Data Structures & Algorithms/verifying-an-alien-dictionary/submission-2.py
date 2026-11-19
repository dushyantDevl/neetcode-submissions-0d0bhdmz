class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        newOrderMap = {order[i]:i for i in range(26)}
        wordsLen = len(words)

        for i in range(wordsLen-1):
            # compare the two consequtive time (since comparing all words at once isn't possible here)
            word1, word2 = words[i], words[i+1]

            for idx in range(len(word1)):
                if idx == len(word2):
                    return False

                ## if first different character has wrong order then just return false, if not
                if word1[idx] != word2[idx]:
                    if newOrderMap[word1[idx]] > newOrderMap[word2[idx]]:
                        return False
                
                ## then `break` bcoz then the order doesn't matter
                    else: 
                        break

        
        return True