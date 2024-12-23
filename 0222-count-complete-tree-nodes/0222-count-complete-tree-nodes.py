# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 0
            
            left = rec(node.left)
            right = rec(node.right)
            return 1 + left + right
        
        return rec(root)