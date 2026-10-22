class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        list_w = list(word)
        list_w.reverse()
        #print(f'insert {list_w}')
        node = self.root
        while list_w:
            current = list_w.pop()
            if current not in node.children.keys():
                insert = TrieNode()
                if not list_w:    
                    insert.is_end = True
                node.children[current] = insert
            else:
                if not list_w:
                    node.children[current].is_end = True
            node = node.children[current]

    def search(self, word: str) -> bool:
        list_w = list(word)
        list_w.reverse()
        #print(f'search on {list_w}')
        node = self.root
        while list_w:
            current = list_w.pop()
            if current not in node.children.keys(): return False
            if not list_w:
                if not node.children[current].is_end: return False
            node = node.children[current]
        return True

    def startsWith(self, prefix: str) -> bool:
        list_w = list(prefix)
        list_w.reverse()
        #print(f'startsWith on {list_w}')
        node = self.root
        while list_w:
            current = list_w.pop()
            if current not in node.children.keys(): return False
            node = node.children[current]
        return True
        