# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(node):
            if not node:
                return None
            if node.val > p.val and node.val > q.val:
                return rec(node.left)
            elif node.val < p.val and node.val < q.val:
                return rec(node.right)
            
            return node
        
        return rec(root)