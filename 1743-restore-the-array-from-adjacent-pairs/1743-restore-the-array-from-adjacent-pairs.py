class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        cnt = defaultdict(int)
        for x,y in adjacentPairs:
            adj[x].append(y)
            adj[y].append(x)
            cnt[x] += 1
            cnt[y] += 1
        # print(adj)
        src = float("inf")
        for key in adj:
            if len(adj[key]) == 1:
                src = key
                break
        s,ans = set(), []
        
        while src not in s:
            # print(src)
            s.add(src)
            ans.append(src)
            for nextt in adj[src]:
                if nextt != src and nextt not in s:
                    src = nextt
                    break
        return ans
            