# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output_arr=[]
        sub_arr=[]
        queue=deque([root])
        while queue:
            sub_arr=[]
            for _ in range(len(queue)):
                
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                sub_arr.append(curr.val)
            output_arr.append(sub_arr)
        return output_arr


        