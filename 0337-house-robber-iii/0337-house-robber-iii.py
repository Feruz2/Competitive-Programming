# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def rec(node,can):
            if not node:
                return 0
            profit = 0
            if can:
                profit = node.val + rec(node.left,0) + rec(node.right,0)
            profit = max(profit,rec(node.left,1) + rec(node.right,1))
            return profit
        return rec(root,1)