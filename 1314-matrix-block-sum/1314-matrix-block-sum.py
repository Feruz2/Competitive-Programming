"""
0 0 
- 1  1

[1,2,3]    6
[4,5,6]    15
[7,8,9]    24

12  15
0   2
1  3
[1, 3, 6]
[4, 9,15]
[7,15,24] 

[12,21,16]
[27,45,33]
[24,39,28]

"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pre = []
        for i in range(len(mat)):
            cnt = 0
            lst = []
            for j in range(len(mat[0])):
                cnt += mat[i][j]
                lst.append(cnt)
            pre.append(lst)
            
        col_pre = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        
        for i in range(len(mat[0])):
            cnt = 0
            lst = []
            for j in range(len(mat)):
                cnt += pre[j][i]
                
                col_pre[j][i] = cnt
                     
        final = []
        # print(pre,col_pre)
        for i in range(len(mat)):
            lst = []
            for j in range(len(mat[0])):
                up = i - k if i - k >= 0 else 0
                down = i + k if i + k < len(mat) else len(mat) - 1
                
                left = j - k if j - k >= 0 else 0
                right = j + k if j + k < len(mat[0]) else len(mat[0]) - 1
                
                ans = col_pre[down][right]
                
                if up > 0:
                    ans -= col_pre[up-1][right] 
                    
                    
                if left > 0:
                    x = col_pre[down][left-1] 
                    if up > 0: x -= col_pre[up-1][left - 1] 
                    
                    ans -= x
                        
                lst.append(ans)
            final.append(lst)
        return final
        
        