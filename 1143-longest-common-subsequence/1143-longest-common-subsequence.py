class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = defaultdict()
        def rec(idx1, idx2):
            # print(idx1, idx2)
            if (idx1, idx2) in dp:
                return dp[(idx1, idx2)]
            
            if idx1 >= len(text1) or idx2 >= len(text2):
                # print("inside", idx1, idx2, st)
                return 0
        
            
            ans = 0
            if text1[idx1] == text2[idx2]:
                ans = max(ans, 1 + rec(idx1 + 1, idx2 + 1))
            else:
                ans = max(ans, rec(idx1 + 1, idx2))
                ans = max(ans, rec(idx1, idx2 + 1))
            
            dp[(idx1, idx2)] = ans
            return ans
        
        
        return rec(0, 0)