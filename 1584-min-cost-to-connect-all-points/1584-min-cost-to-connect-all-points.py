class Union:
    def __init__(self,n):
        self.par = [0]*n
        for i in range(n):
            self.par[i] = i
        
    def find(self,x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unify(self,x,y):
        parx = self.find(self.par[x])
        pary = self.find(self.par[y])
        self.par[x] = pary
        return self.par[x]
        


class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int: 
        union = Union(len(points))
        summ = 0
        n = 0
        start = 0
        heap = []

        for j in range(1,len(points)):

            valx = abs(points[0][0] - points[j][0])
            valy = abs(points[0][1] - points[j][1])
            heapq.heappush(heap,(valx+valy,j))
        
        
        while heap and n < len(points) - 1:
            val, idx  = heappop(heap)
            if union.find(idx) != union.find(start):
                n += 1
                union.unify(idx,start)
                start = idx
                summ += val
                for j in range(len(points)):
                    if j != start and union.find(j) != union.find(start):
                        valx = abs(points[start][0] - points[j][0])
                        valy = abs(points[start][1] - points[j][1])
                        heapq.heappush(heap,(valx+valy,j))

        return summ
            

            
                    
    