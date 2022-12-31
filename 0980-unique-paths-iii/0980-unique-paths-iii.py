class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        in_bound = lambda row,col : 0 <= row< len(grid) and 0 <= col < len(grid[0])
        DIR = [(1,0),(0,1),(0,-1),(-1,0)]
        self.ans = 0
        self.total = 0
        visit = set()
        def dfs(row,col,cnt):
            print(row,col)
            if grid[row][col] == 2 and cnt == self.total:
                self.ans += 1
                return 
            if grid[row][col] == 2:
                print(cnt)
                return 
            if  grid[row][col] == -1: 
                return
            
            for dr,dc in DIR:
                new_r = row + dr
                new_c = col + dc
                if in_bound(new_r, new_c) and (new_r,new_c) not in visit: 
                    visit.add((new_r,new_c))
                    dfs(new_r,new_c,cnt + 1)
                    visit.remove((new_r,new_c))
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i,j)
                    
                elif grid[i][j] != -1:
                    self.total += 1
        visit.add((start[0],start[1]))
        dfs(start[0],start[1],0)
        return self.ans