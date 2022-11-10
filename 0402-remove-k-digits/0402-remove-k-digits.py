class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []
        for i in range(len(num)):
            while s and int(s[-1]) > int(num[i]) and k:
                k -= 1
                s.pop()
            s.append(num[i])
            if k == 0:
                # print(s,i)
                s.extend(num[i+1:])
                break
        if k:
            s = s[:len(s) - k]
        ans = "".join(s)
        if ans != "":ans = str(int(ans))
        return ans if ans != "" else "0"