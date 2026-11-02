class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Time complexity: Loop over prices O(n)
        # Space complexity: Fixed number of variables O(1)
        maxProfit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy: 
                buy = prices[i]
            else:
                maxProfit += prices[i] - buy
                buy = prices[i]
        
        return maxProfit