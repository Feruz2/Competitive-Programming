class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        in_bound = lambda row ,col : 0<=row<m and 0<=col<n
        grid = [] 
        for i in range(m):
            lst = []
            for j in range(n):
                lst.append(1)
            grid.append(lst)
            
        for r,c in guards:
            grid[r][c] = 2
        for r,c in walls:
            grid[r][c] = 3
            
        for row,col in guards:
            for i in range(col+1,n):
                if not in_bound(row,i) or grid[row][i] == 3 or grid[row][i] ==2:
                    break
                grid[row][i] =0
            for i in range(col-1,-1,-1):
                if not in_bound(row,i) or grid[row][i] == 3 or grid[row][i] ==2:
                    break
                grid[row][i] =0
            for i in range(row+1,m):
                if not in_bound(i,col) or grid[i][col] == 3 or grid[i][col] ==2:
                    break
                grid[i][col] =0
            for i in range(row-1,-1,-1):
                if not in_bound(i,col) or grid[i][col] == 3 or grid[i][col] ==2:
                    break
                grid[i][col] =0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count