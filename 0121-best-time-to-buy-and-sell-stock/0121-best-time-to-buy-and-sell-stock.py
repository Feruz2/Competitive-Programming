class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        ma = float("-inf")
        for i in range(len(prices) - 1,-1,-1):
            ans = max(ans,ma - prices[i])
            ma = max(ma,prices[i])
        return ans