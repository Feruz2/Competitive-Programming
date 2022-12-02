class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        i = 0
        for x,y in equations:
            adj[x].append((y,values[i]))
            adj[y].append((x,1/values[i]))
            i += 1
        ans = []
        for x, y in queries:
            qu = deque([(x,-1,1)])
            final = -1
            visit = set()
            while qu:
                N = len(qu)
                for i in range(N):
                    node,par,val = qu.popleft()
                    if node == y and node in adj:
                        final = val
                    if node in visit:
                        continue
                    visit.add(node)
                    for nextt in adj[node]:
                        if nextt[0] != par:
                            qu.append((nextt[0], node , val * nextt[1]))
            ans.append(float(final))
        return ans 
                    
