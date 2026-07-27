class Trie:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        d = self.root
        for ch in word:
            if ch not in d.children:
                d.children[ch] = Trie()
            d = d.children[ch]
        d.word = True

    def search(self, word: str) -> bool:
        
        def dfs(j,node):
            d = node
            for i in range(j,len(word)):
                if word[i] == '.':
                    
                    for child in d.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in d.children:
                        return False
                    d = d.children[word[i]]

            return d.word
        return dfs(0,self.root)

                    
                
        
