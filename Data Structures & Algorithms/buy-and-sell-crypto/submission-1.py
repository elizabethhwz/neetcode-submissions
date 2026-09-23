class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minv = prices[0]
        for p in prices:
            maxprofit = max(p - minv, maxprofit)
            minv = min(minv, p)
        return maxprofit
        