class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def rec(idx):
        
            if idx == len(s):
                return 1
            
            one,two = 0,0
            if s[idx] != "0":
                one = rec(idx+1)
            if idx <= len(s) - 2 and s[idx] != "0" and 1 <= int(s[idx:idx+2]) <= 26:
                two = rec(idx+2)
            return  one + two
        return rec(0)