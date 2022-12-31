class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        
        if len(edges) == 0: return max(vals)
        for x,y in edges:
            adj[x].append(vals[y])
            adj[y].append(vals[x])
            
        ans = max(vals)
        
        for key in adj:
            
            adj[key].sort()
            curr = vals[key]
            node = len(adj[key]) - 1
            for i in range(min(k,len(adj[key]))):
            
                if adj[key][node] + curr > curr:
                    curr += adj[key][node]
                node -= 1
            ans = max(curr,ans)
        return ans
                    
                    
                    