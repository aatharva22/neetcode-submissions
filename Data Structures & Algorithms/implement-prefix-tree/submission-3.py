class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        d = self.root

        for ch in word:
            if ch not in d:
                d[ch] = {}
            d = d[ch]
        d['.'] = '.'


    def search(self, word: str) -> bool:
        
        d = self.root
        for ch in word:
            if ch not in d:
                return False
            d = d[ch]
        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for ch in prefix:
            if ch not in d:
                return False
            d = d[ch]
        return True
        
        