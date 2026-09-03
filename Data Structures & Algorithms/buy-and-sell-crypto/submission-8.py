class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, mp = 0, 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            mp = max(mp, prices[r] - prices[l])
        return mp