class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(row):
            visited.add(row)
            
            for i in  range(len(isConnected[row])):
                col = isConnected[row][i]
                if i != row and col == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        ans = 0
        for i in range(len(isConnected)):
            if i not in visited:
                ans += 1
                dfs(i)
        if ans == 0:
            return len(isConnected)
        return ans
            