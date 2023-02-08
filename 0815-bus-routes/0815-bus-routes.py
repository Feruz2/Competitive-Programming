class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        adj = defaultdict(int)
        i = 0
        num = defaultdict(list)
        for r in routes:
            adj[i] = set(r)
            for val in r:
                num[val].append(i)
            i += 1
            
        qu = deque(num[source])
        
        visit = set(num[source])

        ans = 0
        while qu:
            ans += 1
            N = len(qu)
            for i in range(N):
                node = qu.popleft()
                if target in adj[node]:
                    return ans
                for nextt in adj[node]:
                    for see in num[nextt]:
                        if see not in visit:
                            qu.append(see)
                            visit.add(see)
                    
        return -1
                    