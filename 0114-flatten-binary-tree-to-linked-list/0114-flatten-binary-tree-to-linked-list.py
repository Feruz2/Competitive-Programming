# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        st = []
        node =  root
        while st or node:
            if node.left:
                st.append(node)
                node = node.left
                continue
            if node.right:
                node = node.right
                continue
            print(node.val)
            par = None
            if st:
                par = st.pop()
            while st and par.right == None:
                par = st.pop()
            
            if par and par.right != None:    
                node.right = par.right
                node = par.right
                par.right = None
            else:
                break
        node = root
        while node:
            if node.left:
                node.right = node.left
                node.left = None
            node = node.right
            