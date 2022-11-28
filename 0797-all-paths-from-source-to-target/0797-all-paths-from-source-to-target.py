class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ans.append(list(path))
                return None
            for nextt in graph[node]:
                path.append(nextt)
                dfs(nextt,path)
                path.pop()
        dfs(0,[0])
        return ans