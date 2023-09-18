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
#         dicit = defaultdict(list)
        
#         for i in range(len(points)):
        
#             for j in range(len(points)):
#                 if i != j :
#                     valx = abs(points[i][0] - points[j][0])
#                     valy = abs(points[i][1] - points[j][1])
#                     dicit[i].append((valx+valy,j))
#             dicit[i].sort()
     
        union = Union(len(points))
#         print(dicit)
        summ = 0
#         start = points[0] 
#         for i in range(len(points)):
#             for j in range(len(dicit[i])):
#                 if union.find(i) != union.find(dicit[i][j][1]):
#                     union.unify(i,dicit[i][j][1])
#                     print(dicit[i][j][0],i,dicit[i][j][1])
#                     print(union.par)
#                     summ += dicit[i][j][0]
#                     # print(summ)
#                     break
#         return summ
            
        heap = []

        for j in range(1,len(points)):

            valx = abs(points[0][0] - points[j][0])
            valy = abs(points[0][1] - points[j][1])
            heapq.heappush(heap,(valx+valy,j))
        # print(heap)
        n = 0
        start = 0
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
            

            
                    
    