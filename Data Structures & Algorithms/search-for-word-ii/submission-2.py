class Trie:
    def __init__(self):
        self.child={}
        self.is_end=False
    def add_val(self,word):
        c=self
        for w in word:
            if w not in c.child:
                c.child[w]=Trie()
            c=c.child[w]
        c.is_end=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()
        for w in words:
            root.add_val(w)
        res=set()
        rows,cols=len(board),len(board[0])
        visit=set()

        def backtrack(r,c,node,word):
            if (r<0 or c<0 or r==rows or c ==cols or (r,c) in visit or board[r][c] not in node.child):
                return 
            visit.add((r,c))
            node=node.child[board[r][c]]
            word+=board[r][c]
            if node.is_end:
                res.add(word)
            backtrack(r+1,c,node,word)
            backtrack(r-1,c,node,word)
            backtrack(r,c+1,node,word)
            backtrack(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c,root,"")
        return list(res)



        

        