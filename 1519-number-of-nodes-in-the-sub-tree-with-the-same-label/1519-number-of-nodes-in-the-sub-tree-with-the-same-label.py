class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        ans = [0] * n  
        
        def dfs(node,par):
            hashMap =  Counter()
            for nextt in adj[node]:
                if nextt != par:
                    
                    hashMap += dfs(nextt, node)
                    
            hashMap[labels[node]] += 1
            ans[node] = hashMap[labels[node]]
            return hashMap
        dfs(0,-1)
        return ans