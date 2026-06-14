class MinStack:

    def __init__(self):
        self.stack=[]
        self.top_ele=-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top_ele+=1
        

    def pop(self) -> None:
        del self.stack[self.top_ele]
        self.top_ele-=1
        

    def top(self) -> int:
        return self.stack[self.top_ele]
        

    def getMin(self) -> int:
        
        return min(self.stack)
        
