class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        if 0 == amount:
            return 0
#         @cache
#         def rec(idx,sofar):

#             # if sofar == 0:
#             #     return 1
#             if sofar < 0:
#                 return float("inf")
#             if idx <= 0:
                
#                 if sofar % coins[idx] == 0:
#                     return ((sofar) // coins[idx])
#                 return float("inf")
            
#             return min(1 + rec(idx,sofar - coins[idx]), rec(idx - 1,sofar))
        
#         ans = rec(len(coins) - 1,amount)
#         return ans 
        dp = []
        for i in range(len(coins)):
            new_row = []
            for j in range(amount + 1):
                new_row.append(0)
            dp.append(new_row)
            
        for i in range(1,amount+1):
            if (i) % coins[0] == 0:
                dp[0][i] = i//coins[0]
            else:
                dp[0][i] = float('inf')
                
        for i in range(1,len(coins)):
            for j in range(amount + 1):
                not_take = dp[i-1][j]
                take = float('inf')
                if j >= coins[i]:
                    take = 1 + dp[i][j-coins[i]]
                dp[i][j] = min(take,not_take)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1