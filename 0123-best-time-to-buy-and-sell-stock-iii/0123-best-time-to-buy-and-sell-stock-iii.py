class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @cache
        # def rec(idx, canBuy, cap):
        #     if cap == 0:
        #         return 0
        #     if idx == len(prices):
        #         return 0
        #     if canBuy:
        #         profit = max(-prices[idx] + rec(idx + 1, 0, cap), 0 + rec(idx + 1, 1, cap))
        #     else:
        #         profit = max(prices[idx] + rec(idx + 1, 1, cap - 1), 0 + rec(idx + 1, 0, cap))
        #     return profit
        # return rec(0, 1, 2)
        dp = [[0,0,0],[0,0,0]]
        curr = [[0,0,0],[0,0,0]]

        for idx in range(len(prices) - 1,-1,-1):
            for canBuy in range(2):
                for cap in range(2,0,-1):

                    if canBuy:
                        profit = max(-prices[idx] + dp[0][cap], 0 + dp[1][cap])
                    else:
                        profit = max(prices[idx] + dp[1][cap - 1], 0 + dp[0][cap])
                    curr[canBuy][cap] = profit
            dp = curr
            
        # print(dp)
        return dp[1][2]
                
                