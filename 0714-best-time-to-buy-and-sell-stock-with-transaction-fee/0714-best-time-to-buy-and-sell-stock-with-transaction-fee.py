class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def rec(idx,buy):
            if idx == len(prices):
                return 0
            if buy:
                profile = max(-prices[idx] + rec(idx + 1, 0), 0 + rec(idx + 1,1))
            else:
                profile = max(prices[idx] - fee + rec(idx + 1, 1) , 0 + rec(idx + 1,0))
            return profile
        return rec(0,1)