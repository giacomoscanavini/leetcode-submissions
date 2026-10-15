class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        minDiff = float('inf')
        closestSum = 0
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(minDiff): 
                    minDiff = total - target
                    closestSum = total
                if total < target:
                    left += 1
                elif total > target: 
                    right -= 1
                else:
                    return total

            if nums[i] > 0 and target < nums[i] + nums[i+1] + nums[i+2]: break

        return closestSum