class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prof = 0
        if n == 1: return prof
        if n == 2:
            return max(prof, prices[1] - prices[0])
        i = 0
        buy = prices[i]
        sell = max(prices[i+1:])
        prof = max(prof, sell-buy)
        prof = max(prof, self.maxProfit(prices[i+1:]))
        return prof