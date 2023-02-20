class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        dot = queryIP.count(".")
        colon = queryIP.count(":")
        if colon == 0 and dot == 3:
            arr = [i for i in queryIP.split(".")]
            flag = True
            for i in arr:
                if i.isdigit() and int(i) <= 255:
                    x = int(i)
                    if str(x) != i:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                return "IPv4"
            else:
                return "Neither"
        elif colon == 7 and dot == 0:
            flag = True
            arr = [i for i in queryIP.split(":")]
            for parts in arr:
                l = 0
                for i in parts:
                    l += 1
                    if i not in "0123456789abcdefABCDEF":
                        flag = False
                        break
                if l > 4 or l < 1:flag = False;break
            if flag:
                return "IPv6"
            else:
                return "Neither"

        else:
            return "Neither"