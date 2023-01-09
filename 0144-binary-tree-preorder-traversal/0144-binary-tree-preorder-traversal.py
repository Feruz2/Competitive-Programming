# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = root
        arr = []
        while temp:
            if temp.left:
                node = temp.left
                while node.right and node.right != temp:
                    node = node.right
                if node.right == temp:
                    # arr.append(temp.val)
                    temp = temp.right
                    # node.right = None
                else:
                    node.right = temp
                    arr.append(temp.val)
                    temp = temp.left
            else:
                arr.append(temp.val)
                temp =  temp.right
        return arr