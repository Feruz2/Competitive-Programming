class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def rec(idx1,idx2):
            if idx2 == len(t):
                return 1
            if idx1 == len(s):
                return 0
            one = 0
            if s[idx1] == t[idx2]:
                one = rec(idx1 + 1,idx2 + 1)
            return rec(idx1+1,idx2) + one
        return rec(0,0)