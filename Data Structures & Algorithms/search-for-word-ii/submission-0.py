class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        res, vis = set(), set()
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(r, c, node, currWord):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in vis or
                board[r][c] not in node.children
            ):
                return
            
            vis.add((r,c))
            node = node.children[board[r][c]]
            currWord += board[r][c]

            if node.endOfWord: res.add(currWord)

            # Check in all 4 direction
            dfs(r, c+1, node, currWord)
            dfs(r+1, c, node, currWord)
            dfs(r, c-1, node, currWord)
            dfs(r-1, c, node, currWord)

            vis.remove((r,c)) # mark as not visited while backtracking

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)