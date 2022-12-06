# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(node):
            if not node:
                return None
            
            node.left = rec(node.left)
            node.right = rec(node.right)
            if not node.right and not node.left and node.val == target:
                return None
            return node
        return rec(root)