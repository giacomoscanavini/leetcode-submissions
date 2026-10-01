class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1: return 0

        maximum = 0
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if prices[i] - buy > maximum: 
                maximum = prices[i] - buy
                sell = prices[i]
                
            if prices[i] < buy: 
                buy = prices[i]
                
        return maximum