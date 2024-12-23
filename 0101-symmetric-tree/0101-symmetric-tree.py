# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def rec(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            
            return node2.val == node1.val and rec(node1.right, node2.left) and rec(node1.left, node2.right)
        
        return rec(root.left, root.right)