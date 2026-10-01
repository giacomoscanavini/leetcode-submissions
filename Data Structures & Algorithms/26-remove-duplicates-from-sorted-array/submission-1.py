class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m = len(nums)
        i, k = 0, 0

        while m > 0:
            if i == 0:
                m -= 1
                i += 1
                k += 1
            else:
                if nums[i] == nums[i-1]:
                    del nums[i]
                    nums.append('_')
                    m -= 1

                else:
                    k += 1
                    i += 1
                    m -= 1
        
        return k
