class Solution:
    def rob(self, nums: list[int]) -> int:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create fixed number of variables O(1) 
        # n is len(nums)

        # Edge cases
        if len(nums) == 1: return nums[0]

        # Define starting houses
        a, b = nums[0], nums[1]
        for i in range(2, len(nums)):
            # Apply recursiveness in which we store the path with most money in a
            # And we update the one path that is at least 1 house away
            a, b = max(a, b), a + nums[i]

        return max(a, b)