# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def rec(node):
            if not node:
                return (0,0)
            
            leftK, totalL = rec(node.left)
            rightK, totalR = rec(node.right)
            
            return (max(leftK, rightK) + 1, max(totalL, totalR, leftK + rightK))
                    
        one, two = rec(root)
        return max(one - 1, two)