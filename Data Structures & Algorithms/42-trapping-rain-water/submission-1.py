class Solution:
    def trap(self, height):
        # Time complexity: Loop over height O(n)
        # Space complexity: Fixed number of variables O(1)
        maxL, maxR = 0, 0
        water = 0
        h = 0
        l, r = 0, len(height)-1
        while l < r: 
            if height[l] > maxL: maxL = height[l]
            if height[r] > maxR: maxR = height[r]
            if maxL < maxR: 
                water += maxL - height[l]
                l += 1
            else: 
                water += maxR - height[r]
                r -= 1

        return water