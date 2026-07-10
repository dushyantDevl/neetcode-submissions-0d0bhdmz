class TrieNode:

    def __init__(self) -> None:
        self.child = {}
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(idx, currChild): # idx represent the remaining substring of word 
            curr = currChild
            for i in range(idx, len(word)):
                char = word[i]

                ## here we can simply use iterative method to check for each alphabet from word in the
                ## required TrieNodes
                if char != '.':
                    if char not in curr.child:
                        return False
                    curr = curr.child[char]
                else: # has to use recursive approach (backtrack) to check for all required TrieNodes
                    for child in curr.child.values():
                        if dfs(i+1, child): # skip the '.' and look for next char (@ i+1)
                            return True
                    return False
            return curr.endOfWord

        return dfs(0, self.root)

