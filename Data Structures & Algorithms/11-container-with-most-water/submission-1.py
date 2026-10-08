class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        i = 0
        j = len(height) - 1
        while i < j: 
            minHeight = min(height[i], height[j])
            maxWater = max(maxWater, int(minHeight * (j - i)))
            print(height[i], height[j], maxWater)

            if height[i] > height[j]: 
                j -= 1
            else:
                i += 1    
        return maxWater

