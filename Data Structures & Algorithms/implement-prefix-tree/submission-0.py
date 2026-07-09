class PrefixTree:

    def __init__(self):
        self.trie = set()        

    def insert(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        if word in self.trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.trie:
            if word.startswith(prefix):
                return True

        return False
        