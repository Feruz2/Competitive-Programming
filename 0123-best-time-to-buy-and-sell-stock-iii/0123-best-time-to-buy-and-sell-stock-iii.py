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
        dp = []
        for i in range(len(prices) + 1):
            new = []
            for j in range(2):
                l = []
                for k in range(2+1):
                    l.append(0)
                new.append(l)
            dp.append(new)

        for idx in range(len(prices) - 1,-1,-1):
            for canBuy in range(2):
                for cap in range(2,0,-1):


                    if canBuy:
                        profit = max(-prices[idx] + dp[idx + 1][0][cap], 0 + dp[idx + 1][1][cap])
                    else:
                        profit = max(prices[idx] + dp[idx + 1][1][cap - 1], 0 + dp[idx + 1][0][cap])
                    dp[idx][canBuy][cap] = profit
        # print(dp)
        return dp[0][1][2]
                
                