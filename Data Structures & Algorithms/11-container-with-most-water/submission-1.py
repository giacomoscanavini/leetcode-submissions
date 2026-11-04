class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Time complexity: Loop over height O(n)
        # Space complexity: Fixed number of variables O(1)
        water = 0
        l, r = 0, len(height)-1
        while l < r: 
            h = min(height[l], height[r])
            w = r - l
            water = max(water, h * w)
            if height[l] > height[r]: r -= 1
            else: l += 1

        return water