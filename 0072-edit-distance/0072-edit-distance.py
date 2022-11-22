class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp  = [[0]*(len(word1) + 1) for _ in range(len(word2) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = i
                if i == 0:
                    dp[i][j] = j
                    
        for idx2 in range(1,len(dp)):
            for idx1 in range(1,len(dp[i])):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    dp[idx2][idx1] = dp[idx2 - 1][idx1 - 1]
                else:
                    dp[idx2][idx1] =  1 + min(dp[idx2-1][idx1-1],dp[idx2-1][idx1],dp[idx2][idx1-1])
        return dp[-1][-1]
    
