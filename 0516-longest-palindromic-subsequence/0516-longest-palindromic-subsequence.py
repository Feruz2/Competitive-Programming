class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = []
        t = s[::-1]
        for i in range(len(s)+1):
            new = []
            for j in range(len(s)+1):
                new.append(0)
            dp.append(new)
        
        for idx1 in range(len(s) - 1,-1,-1):
            for idx2 in range(len(s) - 1,-1,-1):

                if s[idx1] == t[idx2]:
                     dp[idx1][idx2] = 1 + dp[idx1+1][idx2+1]
                else:
                      dp[idx1][idx2] =max(dp[idx1+1][idx2],dp[idx1][idx2+1])


        return dp[0][0]