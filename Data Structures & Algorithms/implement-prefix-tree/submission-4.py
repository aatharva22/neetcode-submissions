class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        d = self.root

        for ch in word:
            if ch not in d.children:
                d.children[ch] = TrieNode()
            d = d.children[ch]
        d.word = True
                

    def search(self, word: str) -> bool:

        d = self.root
        for ch in word:
            if ch not in d.children:
                return False
            d = d.children[ch]
        return d.word
        

    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for ch in prefix:
            if ch not in d.children:
                return False
            d = d.children[ch]
        return True
        
        