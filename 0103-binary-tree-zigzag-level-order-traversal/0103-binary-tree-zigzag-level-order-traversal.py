# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: return []
        qu = [[root]]
        ans = []
        flag = True
        while qu:
            level = qu.pop()
            childs = []
            temp = []
            for i in range(len(level)):
                temp.append(level[i].val)
                if level[i].left: 
                    childs.append(level[i].left)
                if level[i].right: 
                    childs.append(level[i].right)
            
            if flag:
                    ans.append(temp)
                    flag = False
            else:
                ans.append(temp[::-1])
                flag = True
                    
            if childs:
                qu.append(childs)
                
        print(ans)
        return ans
            
            
            