class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        dp = []
        for i in range(len(s)+1):
            n = []
            for j in range(len(s)+1):
                n.append(0)
            dp.append(n)
        for idx1 in range(len(s) - 1, -1, -1):
            for idx2 in range(len(s) - 1,-1,-1):
               
                if s[idx1] == t[idx2]:
                    dp[idx1][idx2] = 1 + dp[idx1 + 1][idx2 + 1]
                else:        
                    dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])
        return dp[0][0]
                    