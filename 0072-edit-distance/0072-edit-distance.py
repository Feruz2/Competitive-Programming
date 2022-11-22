class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def rec(idx1, idx2):
            if idx1 < 0 :
                return idx2 + 1
            if idx2 < 0:
                return idx1 + 1
            if word1[idx1] == word2[idx2]:
                return rec(idx1 - 1,idx2 - 1)
            return 1 + min(rec(idx1 -1,idx2 - 1),rec(idx1 - 1,idx2),rec(idx1,idx2-1))
        return rec(len(word1)-1,len(word2)-1)