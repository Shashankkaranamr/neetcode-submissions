class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=["+","-","*","/"]
        for char in tokens:
            if char not in operations:
               
                stack.append(int(char))
            else:
                s1=stack.pop()
                s2=stack.pop()
                if char=="+":
                    r=s2+s1
                elif char=="*":
                    r=s2*s1
                elif char=="-":
                    r=s2-s1
                elif char=="/":
                    r=int(s2/s1)
                stack.append(r)
        return int(stack.pop())

            