# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0

        def node(root):
            if not root:
                return 0
            curr=root
            max_left=node(curr.left)
            max_right=node(curr.right)

            self.max_diameter=max(self.max_diameter,max_left+max_right)
            return 1+max(max_left,max_right)
        node(root)
        return self.max_diameter
        
        