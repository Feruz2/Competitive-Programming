class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @cache
        def rec(idx, canBuy, cap):
            if cap == 0:
                return 0
            if idx == len(prices):
                return 0
            if canBuy:
                profit = max(-prices[idx] + rec(idx + 1, 0, cap), 0 + rec(idx + 1, 1, cap))
            else:
                profit = max(prices[idx] + rec(idx + 1, 1, cap - 1), 0 + rec(idx + 1, 0, cap))
            return profit
        return rec(0, 1, k)