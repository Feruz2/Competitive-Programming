class Solution:
    def maxProfit(self, prices: List[int]) -> int:

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
        print(dp)
        return dp[0][1]