class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def rec(idx):
            if idx == len(s):
                return 1
            if idx > len(s):
                return 0
            one = two = 0
            if s[idx] != "0":
                one = rec(idx+1) 
            if s[idx] != "0" and int(s[idx:idx+2]) < 27:
                two = rec(idx+2)
            return one + two
        return rec(0)
        