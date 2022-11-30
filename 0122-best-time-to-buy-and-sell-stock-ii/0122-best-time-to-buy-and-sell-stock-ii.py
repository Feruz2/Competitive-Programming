class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        dp = [0,0]
        curr = [0,0]  
        for idx in range(len(prices) - 1, -1, -1):
            for j in range(2):
                if j:
                    profit = max(-prices[idx] + dp[0], 0 + dp[1])
                else:
                    profit = max(prices[idx] + dp[1], 0 + dp[0])
                curr[j] = profit
            dp = curr
        return dp[1]       