class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dicit = defaultdict(int)
        for word in wordDict:
            dicit[word] += 1
        memo = defaultdict(bool)
        def rec(st,idx):
            
            if (st, idx) in memo:
                return memo[(st,idx)]
            
            if idx >= len(s):
                if st in dicit:
                    
                    return True
                return False
                
            
            for i in range(idx, len(s)):
                if st in dicit:
                    
                    memo[(st,idx)] = rec(st + s[i], i + 1) or rec(s[i], i + 1)
                    return memo[(st,idx)]
                memo[(st,idx)] = rec(st + s[i], i + 1)
                return memo[(st,idx)]
                    
            
        return rec("",0)