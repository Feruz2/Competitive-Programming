class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        inbound = lambda row,col : 0<=row<len(board) and 0<= col < len(board[0]) - 1
        qu = deque()
        lst = set()
        visit = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i])- 1:
                    if board[i][j] == "O":
                        lst.add((i,j))
                        qu.append((i,j))
                        visit.add((i,j))
        
        while qu:
            row,col = qu.popleft()                                                     
            for newRow, newCol in [(row + 1,col),(row,col-1),(row-1,col),(row,col+1)]:
                if inbound(newRow,newCol) and board[newRow][newCol] == "O" and (newRow,newCol) not in visit:
                    visit.add((newRow,newCol))
                    lst.add((newRow,newCol))                                   
                    qu.append((newRow,newCol))
        # print(lst)                                                              
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]  == "O" and (i,j) not in lst:
                    board[i][j] = "X"
        return board
                
                                                                       
        
        