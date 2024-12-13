class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def rec(countOpen, countClose, n, st):
            if countClose > countOpen:
                return
            if countClose + countOpen == n:
                if countClose == countOpen:
                    ans.append(st)
                return
            rec(countOpen + 1, countClose, n, st + '(')
            rec(countOpen, countClose + 1, n, st + ')')
        
        rec(0, 0, n * 2 ,'')
        return ans