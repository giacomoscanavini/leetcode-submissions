class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Time complexity: Loop over all values up to amount, loop over usable coins O(n * k)
        # Space complexity: Create array of states O(n)
        # n is the value of amount

        # Clean up the coins list by removing all those coins not needed
        coins = set(coins)
        remove_coins = set()
        for c in coins:
            if c > amount: remove_coins.add(c)
        coins = coins.difference(remove_coins)

        # Create state array initializing with the coins
        dp = [0] * (amount + 1)
        for c in coins: dp[c] = 1

        # Bottom-up evaluate each value up to amount
        for val in range(1, amount + 1):
            minNum = float('inf')
            for c in coins:
                # Test each coin, compare minimum number of coins to be at that state
                if val - c >= 0: minNum = min(minNum, dp[val-c]+1)
            dp[val] = minNum

        if dp[-1] == float('inf'): return -1
        else: return dp[-1]