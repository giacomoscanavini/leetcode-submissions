class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif total < 0:
                    j += 1
                
                else:
                    k -= 1

        return output