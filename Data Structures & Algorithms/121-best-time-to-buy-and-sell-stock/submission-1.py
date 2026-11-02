class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Time complexity: Loop over prices O(n)
        # Space complexity: Fixed number of variables O(1)
        buy = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < buy: 
                buy = prices[i]
            else:
                maxProfit = max(maxProfit, prices[i] - buy)

        return maxProfit