class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]

            for j in range(len(w1)):
                # w1 is bigger even tho from 0 to j-1 the characters were same for both w1 & w2
                if j == len(w2): 
                    return False

                if w1[j] != w2[j]: # Look for first different character
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
        return True