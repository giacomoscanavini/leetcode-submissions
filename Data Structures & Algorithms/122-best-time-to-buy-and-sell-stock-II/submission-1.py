class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Time complexity: Loop over prices O(n)
        # Space complexity: Create fixed number of variables O(1)
        # n is len(prices)

        # If I have and price is higher --> sell and rebuy
        # If I have and price is lower  --> replay buy
        # If I don't have --> buy

        # Loop over the prices
        buy = float('inf')
        sell = 0
        for price in prices:
            if buy < price: 
                sell += (price - buy)
                buy = price
            else:
                buy = price

        return sell