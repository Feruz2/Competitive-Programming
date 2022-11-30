class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(idx,canBuy):
            
            if idx == len(prices):
                return 0
            if canBuy:
                profit = max(-prices[idx] + rec(idx + 1,0), 0 + rec(idx + 1,1))
            else:
                profit = max(prices[idx] + rec(idx + 1,1), 0 + rec(idx + 1,0))
            return profit
        return rec(0,1)