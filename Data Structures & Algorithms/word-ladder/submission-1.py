class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordListSet = set(wordList)
        # Optimization: If endWord is not in the list, no solution exists
        if endWord not in wordListSet:
            return 0
            
        q = deque()
        q.append((beginWord, 1))
        
        # Remove beginWord if present to avoid cycles
        if beginWord in wordListSet:
            wordListSet.remove(beginWord)
        
        while q:
            word, lvl = q.popleft()
            if word == endWord:
                return lvl

            for i in range(len(word)):
                # Iterate through all possible lowercase letters
                for j in range(ord('a'), ord('z')+1):
                    char_to_try = chr(j)
                    
                    # Skip if the character is the same as the original
                    if char_to_try == word[i]:
                        continue
                    
                    # Create a NEW string using slicing (Immutable fix)
                    # word[:i] + new_char + word[i+1:]
                    new_word = word[:i] + char_to_try + word[i+1:]
                    
                    if new_word in wordListSet:
                        if new_word == endWord:
                            return lvl + 1
                        wordListSet.remove(new_word) # Mark visited
                        q.append((new_word, lvl+1))
        
        return 0   