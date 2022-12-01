class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        final = []
        def rec(idx,ans):
            if idx == len(s):
                if len(ans) == 4:
                    new = ""
                    for val in ans:
                        new += val + "."
                    final.append(new[:-1])
                return 
            if 0 <= int(s[idx])<= 255:
                rec(idx+1,ans + [s[idx]])
            if s[idx] != "0" and idx <= len(s) - 2:
                rec(idx+2, ans + [s[idx:idx+2]])
            if idx <= len(s) - 3 and s[idx] != "0" and  0 <= int(s[idx:idx+3]) <= 255:
                rec(idx+3, ans + [s[idx:idx+3]])
        rec(0,[])
        return final