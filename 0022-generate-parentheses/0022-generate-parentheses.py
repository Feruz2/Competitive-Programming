class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(st, opened, closed):
            if opened + closed == (n * 2):
                if opened == closed: ans.append(st)
                return
            if opened > closed:
                rec(st + "(", opened + 1, closed)
                rec(st + ")", opened, closed + 1)
            else:
                rec(st + "(", opened + 1, closed)
        
        rec("", 0, 0)
        return ans