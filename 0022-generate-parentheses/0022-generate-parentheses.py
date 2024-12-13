class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def rec(countOpen, countClose, n, st):
            
            if countClose + countOpen == n:
                ans.append(st)
                return
            
            if countOpen < n // 2:
                rec(countOpen + 1, countClose, n, st + '(')
                
            if countClose < countOpen:
                rec(countOpen, countClose + 1, n, st + ')')
        
        rec(0, 0, n * 2 ,'')
        return ans