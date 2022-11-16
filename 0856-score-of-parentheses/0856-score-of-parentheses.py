class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i]== ")":
                idx, val = stack.pop()
                if val:
                    if stack:
                        stack[-1][1] +=  2*val
                    else:
                        ans += 2*val
                else:
                    if stack:
                        stack[-1][1] += 1
                    else:
                        ans += 1
            else:
                stack.append([i,0])
        return ans