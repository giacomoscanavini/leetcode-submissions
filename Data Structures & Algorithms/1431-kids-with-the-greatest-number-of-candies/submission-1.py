class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [True if x + extraCandies >= max_candies else False for x in candies]