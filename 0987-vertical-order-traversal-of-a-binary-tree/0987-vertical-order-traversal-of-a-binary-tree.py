# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dicit = defaultdict(list)
        qu = deque()
        qu.append((root,0,0))
        while qu:
            N = len(qu)
            # print(qu)
            for i in range(N):
                node,col,row = qu.popleft()
                dicit[col].append((row,node.val))
                if node.left:
                    qu.append((node.left,col-1,row+1))
                if node.right:
                    qu.append((node.right,col+1,row+1))
        final = []
        for key in sorted(dicit.keys()):
            listt = sorted(dicit[key],key = lambda  x:(x[0],x[1]))
            lst = []
            for row,val in listt:
                lst.append(val)
            final.append(lst)
        return final