class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # @cache
#         def dfs(idx,s):
            
#             if  s < 0:
#                 return 0
            
#             if idx == 0:
#                 if (s) % coins[0] == 0:
#                     return 1
                
#                 return 0
#             return dfs(idx,s - coins[idx]) + dfs(idx - 1,s)
            
        
#         return dfs(len(coins) - 1,amount)
        
        dp = []
        for i in range(len(coins)):
            new = []
            for j in range(amount + 1):
                new.append(0)
            dp.append(new)
        for i in range(amount + 1):
            if (i) % coins[0] == 0:
                dp[0][i] = 1
                
        for i in range(1,len(coins)):
            for j in range(amount + 1):
                not_take = dp[i-1][j]
                take = 0
                if j >= coins[i]:
                    take = dp[i][j-coins[i]]
                dp[i][j] = not_take + take
        return dp[-1][-1]