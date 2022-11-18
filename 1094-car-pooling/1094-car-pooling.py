class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = 0
        for i in range(len(trips)):
            
                ans = max(ans,trips[i][1],trips[i][2])
        p = [0] *(ans+1)
        for i in range(len(trips)):
            
            p[trips[i][1]] += trips[i][0]
            p[trips[i][2]] += -1*trips[i][0]
        
        x = 0
        for i in range(len(p)):
            x += p[i]
            p[i] = x
        print(p)
        return max(p) <= capacity 