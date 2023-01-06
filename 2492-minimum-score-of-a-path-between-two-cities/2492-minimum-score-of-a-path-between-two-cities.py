class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x, y, d in roads:
            adj[x].append((y,d))
            adj[y].append((x,d))
        qu = deque([1])
        visit = set()
        ans = float("inf")
        while qu:
            N = len(qu)
            for i in range(N):
                node = qu.popleft()
                if node in visit:
                    continue
                visit.add(node)
                for nextt,distance in adj[node]:
                    qu.append(nextt)
                    ans = min(ans,distance)
        return ans