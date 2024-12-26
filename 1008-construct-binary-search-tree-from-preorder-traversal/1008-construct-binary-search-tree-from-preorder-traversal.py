# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def rec(left, right):
            if self.i >= len(preorder):
                return None
            if left < preorder[self.i] < right:
                curr = TreeNode(preorder[self.i])
                self.i += 1
                curr.left = rec(left, curr.val)
                curr.right = rec(curr.val, right)
                return curr
            else:
                return None
        return rec(float('-inf'), float('inf'))