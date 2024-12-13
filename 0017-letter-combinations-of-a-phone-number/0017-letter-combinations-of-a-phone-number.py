class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        
        ans = []
        dicit = {'2': ['a', 'b', 'c'], 
                 '3': ['d', 'e', 'f'], 
                 '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r','s'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        def rec(idx,st):
            if idx >= len(digits):
                if len(st) == len(digits):
                    ans.append(st)
                return 
            
            for i in range(idx, len(digits)):
                for j in range(len(dicit[digits[i]])):
                    rec(i + 1, st + dicit[digits[i]][j])
        
        rec(0, '')
        return ans