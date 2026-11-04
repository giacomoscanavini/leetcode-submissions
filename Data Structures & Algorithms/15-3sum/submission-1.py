class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time complexity: Loop over nums and two pointers with worst case O(n^2)
        # Space complexity: Output list with worst O(n)
        nums = sorted(nums)
        if nums[0] > 0 or nums[-1] < 0: return []

        output = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue

            target = 0 - nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] > target: r -= 1
                elif nums[l] + nums[r] < target: l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums)-1 and nums[l] == nums[l-1]: l += 1

        return output