class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0]*n
        for x, y in roads:  #O(m)
            indegree[x] += 1
            indegree[y] += 1
        heap = []
        for i in range(len(indegree)): #O(NlogN)
            heappush(heap,(-indegree[i],i))

        start = n
        new_val = [0]*n
        while heap: # O(Nlog)
            val, node = heappop(heap)
            new_val[node] = start 
            start -= 1
        ans = 0
        for x, y in roads: #O(m)
            new_x = new_val[x]
            new_y = new_val[y]
            ans += (new_x + new_y)
        return ans