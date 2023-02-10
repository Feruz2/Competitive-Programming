class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def shift(x,y):
            cnt = 0
            for i in range(len(img1)):
                for j in range(len(img2)):
                    if 0<= i+x < len(img1) and 0<= j+y < len(img1) and img1[i+x][j+y] == img2[i][j] == 1:
                        cnt += 1
            return cnt
        ans = []
        for i in range(-len(img1),len(img1)):
            for j in range(-len(img1),len(img1)):
                ans.append(shift(i,j))
        
        return max(ans)