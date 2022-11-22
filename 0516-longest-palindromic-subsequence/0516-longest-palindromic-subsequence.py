class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def rec(idx1,idx2):
            if idx1 > idx2:
                return 0
            if idx1 == idx2:
                return 1
            
            if s[idx1] == s[idx2]:
                return 2 + rec(idx1 + 1, idx2 - 1)
            return max(rec(idx1 + 1,idx2),rec(idx1,idx2 - 1))
        return rec(0,len(s) - 1)