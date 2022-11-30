class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        se =set(p)
        if s == p:
            return True

        @cache
        def rec(idx1,idx2):
            
            if idx1 == len(s):
                if idx2 == len(p):
                    return True
                elif len(set(p[idx2:])) == 1 and p[idx2] == "*":
                    return True
                return False
            if idx2 == len(p):
                return False
            
            if s[idx1] == p[idx2]:
                return rec(idx1 + 1, idx2 + 1)
            elif p[idx2] == "?":
                return rec(idx1+1,idx2 + 1)
            elif p[idx2] == '*':
                return rec(idx1+1,idx2+1) or rec(idx1+1,idx2) or rec(idx1 , idx2 +1)
            return False
        return rec(0,0)