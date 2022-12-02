# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val == key:
                if not node.left or not node.right:
                    return node.left or node.right
                temp = node.left
                while temp.right:
                    temp = temp.right
                temp.right = node.right
                return node.left
            return node
        return dfs(root)