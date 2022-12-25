class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        def rec(idx,curr,cnt):
            if cnt == 0 and idx >= len(s):
                ans.append(curr[:-1])
                return 
            if idx >= len(s):
                return
            if s[idx] == "0":
                return rec(idx + 1, curr + s[idx] + ".", cnt - 1)
            rec(idx + 1, curr + s[idx] + ".",cnt - 1)
            if len(s) >= idx + 2:
                rec(idx + 2, curr + s[idx:idx+2] + ".", cnt - 1)
            if len(s) >= idx + 3 and 0 <= int(s[idx:idx+3]) <= 255:
                rec(idx + 3 ,curr + s[idx:idx+3] + ".",cnt - 1)
            
            
        rec(0,"",4)
        return ans