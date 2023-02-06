class Solution:
    def racecar(self, target: int) -> int:
        qu = deque([(0,1,0)])
        
        
        while qu:
            
            pos,speed,move = qu.popleft()
            
            if pos == target:
                return move
            
            qu.append((pos + speed, speed * 2, move + 1))
            
            if speed < 0 and pos + speed < target:
                qu.append((pos,1,move + 1))
            elif speed > 0 and pos + speed > target:
                qu.append((pos,-1,move + 1))
                
        return -1
                
        
