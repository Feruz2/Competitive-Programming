# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def rec(node):
            if node == None:
                return None
            
            left = rec(node.left)
            right = rec(node.right)
            ans.append(node.val)
        
        rec(root)
        return ans