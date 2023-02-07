class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        new = instructions
        # DIRL = [(1,0),(-1,0),(0,-1),(0,1)]
        # DIRR = [(1,0),(0,1),(0,-1),(-1,0)]
        # leftToright = {0:0,
        #               1:3,
        #               2:2,
        #               1:3}
        
        dx = 0
        dy = 1
        for move in new:
            if move == "G":
                x += dx
                y +=  dy
            elif move == "L":
                dx, dy = -dy, dx 
            
            elif move == "R":
                dx , dy = dy, -dx
        if x == 0 and y == 0:
            return True
        return (dx, dy) != (0,1)