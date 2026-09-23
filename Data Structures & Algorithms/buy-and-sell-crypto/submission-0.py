class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minv = 101
        for p in prices:
            minv = min(minv, p)
            maxprofit = max(p - minv, maxprofit)
        return maxprofit
        