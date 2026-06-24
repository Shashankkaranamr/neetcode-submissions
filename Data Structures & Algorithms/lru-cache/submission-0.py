class Node:
    def __init__(self,value:int,key:int):
        self.value=value
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add(self,new_node:Node):
        
        prev_node=self.tail.prev
        prev_node.next=new_node
        new_node.next=self.tail
        new_node.prev=prev_node
        self.tail.prev=new_node

    def remove(self,node:Node):
        node.prev.next=node.next
        node.next.prev=node.prev
        

        

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        new_node=Node(value,key)
        self.cache[key]=new_node
        self.add(new_node)
        if len(self.cache)>self.capacity:
            lru=self.head.next
            self.remove(lru)
            del self.cache[lru.key]


        
