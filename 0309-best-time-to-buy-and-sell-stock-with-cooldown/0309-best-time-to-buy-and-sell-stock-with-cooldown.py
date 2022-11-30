class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(idx,buy,cool):
            if idx == len(prices):
                return 0
            if cool:
                profit = rec(idx + 1, buy, 0)
            elif buy:
                profit = max(-prices[idx] + rec(idx + 1, 0,cool), 0 + rec(idx+1,1,cool))
            else:
                profit = max(prices[idx] + rec(idx+1,1,1), 0 + rec(idx + 1, 0,cool))
            return profit
        return rec(0,1,0)