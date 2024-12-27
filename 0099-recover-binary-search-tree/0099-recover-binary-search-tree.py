# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        prev = [None]
        def rec(node):
            if not node:
                return None
            rec(node.left)
            if prev[0] != None and prev[0].val > node.val:
                if not ans:
                    ans.append(prev[0])
                    ans.append(node)
                    
                else:
                    ans.append(node)
            prev[0] = node
            rec(node.right)
        rec(root)
        
        ans[0].val, ans[-1].val = ans[-1].val, ans[0].val
            
            