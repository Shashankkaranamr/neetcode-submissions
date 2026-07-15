class Node:
    def __init__(self):
        self.children=dict()
        self.is_ends_with=False

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        current_node=self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c]=Node()
            current_node=current_node.children[c]

        current_node.is_ends_with=True


    def search(self, word: str) -> bool:
        def helper_search(current_node,i):
            for i in range(i,len(word)):
                c=word[i]
                if c==".":
                    for child_node in current_node.children.values():
                        if helper_search(child_node,i+1):
                                return True
                    return False
                else:
                    if c not in current_node.children:
                        return False
                    current_node=current_node.children[c]
            return current_node.is_ends_with
                
                
    
        return helper_search(self.root,0)


