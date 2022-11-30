class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         @cache
#         def rec(idx,canBuy):
            
#             if idx == len(prices):
#                 return 0
#             if canBuy:
#                 profit = max(-prices[idx] + rec(idx + 1,0), 0 + rec(idx + 1,1))
#             else:
#                 profit = max(prices[idx] + rec(idx + 1,1), 0 + rec(idx + 1,0))
#             return profit
#         return rec(0,1)
        dp = []
        for i in range((len(prices) + 1)):
            new_row = [0,0]
            dp.append(new_row)
                       
        
        for idx in range(len(prices) - 1, -1, -1):
            for j in range(2):
                if j:
                    profit = max(-prices[idx] + dp[idx + 1][0], 0 + dp[idx + 1][1])
                else:
                    profit = max(prices[idx] + dp[idx + 1][1], 0 + dp[idx + 1][0])
                dp[idx][j] = profit
        return dp[0][1]       