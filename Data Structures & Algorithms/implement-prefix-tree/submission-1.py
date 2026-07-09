class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()
            curr = curr.child[char]
        curr.endOfWord = True # curr is pointing to last character in the word now so mark it end

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.child:
                return False
            curr = curr.child[char]
        return True # curr now points to last character of the prefix so return true
        