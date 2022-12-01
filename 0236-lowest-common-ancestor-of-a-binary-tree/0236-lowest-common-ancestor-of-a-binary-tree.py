# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def find(node,t,lst):
            if not node:
                return []
            if node.val == t.val:
                ans = list(lst)
                return ans
            
            return find(node.right,t,lst + "R") + find(node.left,t,lst + "L")
        
        
        
        one = find(root,q,"")
        two = find(root,p,"")
        i = 0
        j = 0
        ans = root
        while i < len(one) and j < len(two):
            if one[i] == two[j]:
                if one[i] == "L":
                    ans = ans.left
                else:
                    ans = ans.right
                i += 1
                j += 1
            else:
                break
        return ans



