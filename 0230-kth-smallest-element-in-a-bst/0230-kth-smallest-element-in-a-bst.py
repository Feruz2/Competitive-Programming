# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        turn = [0]
        ans = [-1]
        
        
        def rec(node, ans):
            
            if turn[0] > k:
                return 
            
            if not node:
                return None
            
            if node.left:
                rec(node.left, ans)              
                
            turn[0] += 1
            if turn[0] == k:
                ans[0] = node.val
            
            if node.right:
                rec(node.right, ans)

        if not root.left and not root.right:
            return root.val
        rec(root, ans)
        return ans[0]