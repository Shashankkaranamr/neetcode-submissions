# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0

        def count_k(node):
            nonlocal count
            if not node:
                return
            left_result=count_k(node.left)
            if left_result:
                return left_result
            count+=1
            if k==count:
                return node
            right_result=count_k(node.right)
            return right_result
        result_node=count_k(root)
        return result_node.val
