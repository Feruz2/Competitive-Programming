class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = [num for num in prices]
        m = float('-inf')
        for i in range(len(prices) - 1,-1,-1):
            m = max(m,prices[i])
            mi[i] = m
        ans = 0
        for i in range(len(prices)):
            ans = max(ans,mi[i] - prices[i] )
        return ans