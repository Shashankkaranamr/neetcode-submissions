# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes=0
        max_value=float("-inf")
        def dfs(root,max_value):
            nonlocal good_nodes
            if not root:
                return 
            curr=root
            if curr.val>=max_value:
                max_value=curr.val
                good_nodes+=1
            dfs(curr.left,max_value)
            dfs(curr.right,max_value)
        dfs(root,max_value)
        return good_nodes

        