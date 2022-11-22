class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
       
        memo = {}
        def dp(i,j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if (i,j) not in memo:
                if word1[i] == word2[j]:
                    memo[(i,j)] = dp(i+1,j+1)
                else:
                    replace = dp(i+1,j+1)
                    delete = dp(i+1,j)
                    insert = dp(i,j+1)
                    memo[(i,j)] = 1+min(replace,delete,insert)
            return memo[(i,j)]
        return dp(0,0)
