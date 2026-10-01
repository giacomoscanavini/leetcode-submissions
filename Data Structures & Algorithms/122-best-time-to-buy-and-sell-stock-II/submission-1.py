class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1: return 0
        
        maximum = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > buy:
                maximum += prices[i] - buy
                buy = prices[i]

            else:
                buy = prices[i]

        return maximum