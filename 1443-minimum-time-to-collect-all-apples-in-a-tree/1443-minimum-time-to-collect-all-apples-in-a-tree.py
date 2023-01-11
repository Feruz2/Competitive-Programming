class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node,par):
           
            
            x = 0
            for nextt in adj[node]:
                if nextt != par:
                    x += dfs(nextt,node)
                    print(x)
            if hasApple[node] or x > 0:
                if node != 0:
                    x += 2
            return x
        
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        # print(adj)
        return dfs(0,-1)
        