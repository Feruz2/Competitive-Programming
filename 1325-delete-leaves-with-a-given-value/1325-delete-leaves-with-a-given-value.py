# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        leaf = []
        par = defaultdict(lambda: TreeNode())
        indegree = defaultdict(int)
        delete_hash = defaultdict(int)
        def rec(node):
            if not node.right and not node.left:
                leaf.append(node)
                return node
            
            if node.left : 
                par[rec(node.left)] = node
                indegree[node] += 1
            if node.right: 
                par[rec(node.right)] = node
                indegree[node] += 1
            return node
        def new_tree(node):
            if not node:
                return None
            if node in delete_hash:
                return None
            node.left = new_tree(node.left)
            node.right = new_tree(node.right)
            return node
        rec(root)
        # print(indegree)
        qu = deque()
        for node in leaf:
            qu.append(node)
        # print(qu)
        
        while qu:
            N = len(qu)
            # print(qu)
            for i in range(N):
                delete = False
                node = qu.popleft()
                if node.val == target:
                    delete = True
                    indegree[par[node]] -= 1
        
                if indegree[par[node]] == 0 and par[node].val == target:
                    qu.append(par[node])
                
                if delete:
                    delete_hash[node] = 1
        # print(delete_hash)
        return new_tree(root)
        