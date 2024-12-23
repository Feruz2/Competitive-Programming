# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def rec(node):
            
            if not node:
                return 0
            if node == target:
                return 1
            
            hasTarget = rec(node.left)
           
            if hasTarget > 0:
                steps = k - hasTarget
                if steps == 0: 
                    ans.append(node.val)
                else:
                    BFS(node.right, steps - 1)
                
                
                return hasTarget + 1
            
            hasTarget = rec(node.right)
            if hasTarget > 0:
                
                steps = k - hasTarget
                if steps == 0: 
                    ans.append(node.val)
                else:
                    BFS(node.left, steps - 1)
                
                
                return hasTarget + 1
            return 0
        
        ans = []
        
        def BFS(node, k):
            
            if node:
                qu = deque([node])
            else: 
                qu= []
            while qu and k >= 0:
                N = len(qu)
                for i in range(N):
                    newNode = qu.popleft()
                    
                    if k == 0: ans.append(newNode.val)
                    if newNode.left: qu.append(newNode.left)
                    if newNode.right: qu.append(newNode.right)
                
                k -= 1
          
        rec(root)
        BFS(target, k)
        return ans