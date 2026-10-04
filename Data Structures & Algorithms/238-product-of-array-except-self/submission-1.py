class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            j = len(nums) - 1 - i
            pref[i] = pref[i - 1] * nums[i - 1]
        suff[j] = suff[j+ 1] * nums[j + 1]

        for i in range(len(nums)):
            pref[i] = pref[i] * suff[i]

        return pref