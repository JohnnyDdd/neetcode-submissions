class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def insertWord(self, word) -> None:
        node = self.root
        for i in range(len(word)):
            cur = word[i]
            if cur not in node.children.keys():
                insert = TrieNode()
                if i == len(word)-1: insert.word = word
                node.children[cur] = insert
            else:
                if i == len(word)-1: node.children[cur].word = word 
            node = node.children[cur]


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = set()
        self.root = TrieNode()
        for word in words:
            self.insertWord(word)
        ym, xm = len(board), len(board[0])

        def dfs(y, x, node, visited):
            ret = set()
            if (y,x) not in visited:
                visited.add((y,x))
                l = board[y][x]
                if l in node.children.keys():
                    ex_word = node.children[l].word
                    if ex_word: 
                        ret.add(ex_word)
                        node.children[l].word = None
                    if y+1 <= ym-1: ret = ret | dfs(y+1,x,node.children[l],visited)
                    if y-1 >= 0: ret    = ret | dfs(y-1,x,node.children[l],visited)
                    if x+1 <= xm-1: ret = ret | dfs(y,x+1,node.children[l],visited)
                    if x-1 >= 0: ret    = ret | dfs(y,x-1,node.children[l],visited)
                visited.discard((y,x))          
            return ret
        
        #print(dfs(0,1))

        for y in range(ym):
            for x in range(xm):
                ret = ret | dfs(y,x,self.root,set())
        return list(ret)
                
                  