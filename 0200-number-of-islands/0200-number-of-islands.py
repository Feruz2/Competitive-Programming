class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        in_bound = lambda row,col : 0 <= row< len(grid) and 0 <= col < len(grid[0])
        def dfs(row,col):
            for newRow , newCol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if in_bound(newRow,newCol) and grid[newRow][newCol] == "1":
                    grid[newRow][newCol] = "0"
                    dfs(newRow,newCol)
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    answer += 1
        return answer