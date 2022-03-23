# Definition
#  for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        qu = deque([root])
        final = []
        
        if root:
            temp = [root.val]
        else:
            temp = []
        while qu:
            N = len(qu)
            # print(temp)
            if len(temp) != 0:
                final.append(max(temp))
            temp = []
            for i in range(N):
                node = qu.popleft()
                if node :
                    if node.left:
                        qu.append(node.left)
                        temp.append(node.left.val)

                    if node.right:
                        qu.append(node.right)
                        temp.append(node.right.val)

        return final
                
                
        