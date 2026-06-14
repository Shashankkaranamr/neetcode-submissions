from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        for b in s:
            if b=="{" or b=="[" or b=="(":
                stack.append(b)
            else:
                if len(stack)!=0:
                    b1=stack.pop()
                else:
                    return False
                if (b==")" and not b1=="(") or (b=="}" and not b1=="{") or (b=="]" and not b1=="["):
                    return False
        if len(stack) !=0:
            return False
        return True
        

        