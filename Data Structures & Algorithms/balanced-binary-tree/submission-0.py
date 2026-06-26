# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root):
            if not root:
                return 0
            
            
            curr=root

            depth_left=depth(curr.left)
            if depth_left==-1:
                return -1
            depth_right=depth(curr.right)
            if depth_right==-1:
                return -1

            if abs(depth_left-depth_right)>1:
                return -1
            return 1+max(depth_left,depth_right)
        return depth(root)!=-1        


        