class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        P = 0
        minBuy = prices[0]
        for sell in prices:
            P = max(P, sell - minBuy)
            minBuy = min(minBuy, sell)
        return P