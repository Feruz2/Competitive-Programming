class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # @cache
        # def rec(i,j):
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
        #     if word1[i] == word2[j]:
        #         return rec(i + 1, j + 1)
        #     delete = 1 + rec(i + 1,j)
        #     insert = 1 + rec(i, j + 1)
        #     replace = 1 + rec(i + 1, j+1)
        #     return min(delete,insert,replace)
        # return rec(0,0)
       
        rec = [[0]*(len(word2) + 1) for _ in range(len(word1)+1)]
        for i in range(len(rec)):
            for j in range(len(rec[i])):
                if i == len(word1) and j == len(word2):
                    continue
                elif i == len(word1):
                    rec[i][j] = len(word2) - j
                elif j == len(word2):
                    rec[i][j] = len(word1) - i
        # print(rec)
        """[
          s  p  a  k  e
        p[0, 0, 0, 0, 0, 4],
        a[0, 0, 0, 0, 0, 3],
        r[0, 0, 0, 0, 0, 2], 
        k[0, 0, 0, 0, 0, 1], 
         [5, 4, 3, 2, 1, 0]]

"""
        for i in range(len(word1) -1,-1,-1 ):
            for j in range(len(word2) - 1,-1,-1):
                if word1[i] == word2[j]:
                    rec[i][j] = rec[i + 1][j + 1]
                    continue
                delete = 1 + rec[i + 1][j]
                insert = 1 + rec[i][j + 1]
                replace = 1 + rec[i + 1][j+1]
                rec[i][j] = min(delete,insert,replace)
       
        return rec[0][0]