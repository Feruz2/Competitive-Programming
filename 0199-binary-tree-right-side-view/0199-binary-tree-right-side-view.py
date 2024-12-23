# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        dicit = defaultdict(int)
        def rec(node, height):
            
            if not node:
                return 
            
            if height not in dicit:
                dicit[height] = node.val
            
            rec(node.right, height + 1)
            
            rec(node.left, height + 1)
            
        rec(root, 0)
        
        
        ans = []
        for key, values in dicit.items():
            ans.append(values)
        return ans