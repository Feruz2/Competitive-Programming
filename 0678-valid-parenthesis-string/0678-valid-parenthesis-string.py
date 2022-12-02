class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i in range(len(s)):
            if s[i] == ")":
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    
                    return False
            elif s[i] == "*":
                s2.append(i)
            else:    
                s1.append(i)
        for i in range(len(s1) - 1,-1,-1):
            if s2 and s1[i] < s2[-1]:
                s2.pop()
            else:
                return False
        return True