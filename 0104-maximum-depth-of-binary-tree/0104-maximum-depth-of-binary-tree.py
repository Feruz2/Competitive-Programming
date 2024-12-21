# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(node):
            if not node:
                return 0
            
            left = 1 + rec(node.left)
            right = 1 + rec(node.right)
            return max(left, right)
        return rec(root)
            