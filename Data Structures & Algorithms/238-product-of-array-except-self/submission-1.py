class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time complexity: Loop over the nums O(n)
        # Space complexity: Create left and right prefix arrays O(n)
        left_pref = [1] * len(nums)
        right_pref = [1] * len(nums)
        for i in range(1, len(nums)):
            left_pref[i] = left_pref[i-1] * nums[i-1]
        
        for j in range(0, len(nums)-1)[::-1]:
            right_pref[j] = right_pref[j+1] * nums[j+1]

        for i in range(len(nums)):
            left_pref[i] = left_pref[i] * right_pref[i]

        return left_pref