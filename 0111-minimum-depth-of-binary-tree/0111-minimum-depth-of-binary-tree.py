# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node.left and not node.right: 
                return 1
            
            x = float('inf')
            y = float('inf')
            if node.left:
                x = dfs(node.left) 
            if node.right:
                y = dfs(node.right)
            # print(x,y)
            return 1 + min(x,y)
        if not root:
            return 0
        return dfs(root)