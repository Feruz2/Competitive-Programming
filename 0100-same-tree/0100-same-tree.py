# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1,node2):
            if node1 and node2:
                return (node1.val == node2.val) and dfs(node1.left,node2.left) and dfs(node1.right,node2.right)       
            return node1 is node2
        return dfs(p,q)
                