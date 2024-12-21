# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        node = root
        while node:
            # print(node.val)
            curr = node
            nextt = node.left
            if node.left:
                curr = curr.left
                node.left = None
                while curr.right:
                    curr = curr.right 
            # print(curr.val)
            if curr == node:
                ans.append(curr.val)
                node = curr.right
                continue
            curr.right = node
            node = nextt or node.right
        return ans