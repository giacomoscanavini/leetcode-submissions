class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m = len(nums)
        i, k = 0, 0
        count = 0

        while m > 0:
            if i == 0:
                k += 1
                i += 1
                m -= 1
                count += 1

            else:
                if nums[i] == nums[i-1]:
                    m -= 1
                    count += 1
                    if count < 3: 
                        k += 1
                        i += 1
                    else: 
                        del nums[i]
                        nums.append('_') 
                else:
                    m -= 1
                    count = 1
                    k += 1
                    i += 1

        return k