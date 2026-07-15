class Node:
    def __init__(self):
        self.children=dict()
        self.is_end_of_word=False
    

class PrefixTree:

    def __init__(self):
        self.root=Node()
        

    def insert(self, word: str) -> None:
        current_node=self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c]=Node()
            current_node=current_node.children[c]

        current_node.is_end_of_word=True



    def search(self, word: str) -> bool:
        current_node=self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node=current_node.children[c]
        if current_node.is_end_of_word==True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current_node=self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node=current_node.children[c]
        return True
        
        