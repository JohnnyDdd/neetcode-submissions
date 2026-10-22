class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children.keys():
                insert = TrieNode()
                node.children[c] = insert
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end
            l = word[i]
            if l == '.':
                for child in node.children.values():
                    if dfs(child, i+1): return True
            else:
                if l in node.children.keys(): 
                    return dfs(node.children[l], i+1)
            return False

        node = self.root     
        return dfs(node, 0)