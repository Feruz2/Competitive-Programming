class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def rec(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return rec(i + 1, j + 1)
            delete = 1 + rec(i + 1,j)
            insert = 1 + rec(i, j + 1)
            replace = 1 + rec(i + 1, j+1)
            return min(delete,insert,replace)
        return rec(0,0)
       
        