class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, l = 0, 0

        for i in range(len(prices)):
            maxP = max(maxP, prices[i] - prices[l])
            if prices[i] < prices[l]:
                l = i
        return maxP