# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue=deque([root])
        result=[]

        while queue:
                curr=queue.popleft()
                if curr:
                    result.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    result.append("N")
        return ",".join(result)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals=data.split(",")
        root=TreeNode(int(vals[0]))

        queue=deque([root])
        i=1
        while queue:
            node=queue.popleft()
            if vals[i]!="N":
                node.left=TreeNode(int(vals[i]))
                queue.append(node.left)
            i+=1
            if vals[i]!="N":
                node.right=TreeNode(int(vals[i]))
                queue.append(node.right)
            i+=1
        return root

       