class Union:
    def __init__(self,grid):
        self.par = defaultdict(tuple)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.par[(i,j)] = (i,j)
                    
    def find(self,rowcol):
        if self.par[rowcol] == rowcol:
            return rowcol
        self.par[rowcol] = self.find(self.par[rowcol])
        return self.par[rowcol]
    
    def union(self,rowp,colp,row,col):
        par1 = self.find((row,col))
        par2 = self.find((rowp,colp))
        if par1 != par2:
            self.par[par1] = par2
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        in_bound = lambda row,col: 0 <= row < len(grid) and 0 <= col <len(grid[0])
        obj = Union(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    if in_bound(i+1,j) and grid[i+1][j] == "1":
                        obj.union(i,j,i+1,j)
                    if in_bound(i,j+1) and grid[i][j+1] == "1":
                        obj.union(i,j,i,j+1)
                    if in_bound(i-1,j) and grid[i-1][j] == "1":
                        obj.union(i,j,i-1,j)
                    if in_bound(i,j-1) and grid[i][j-1] == "1":
                        obj.union(i,j,i,j-1)
        for key in obj.par:
            obj.find(key)
        total = Counter(obj.par.values())
        # print(obj.par)
        answer = 0
        for key in total.items():
            answer += 1
        return answer            
            