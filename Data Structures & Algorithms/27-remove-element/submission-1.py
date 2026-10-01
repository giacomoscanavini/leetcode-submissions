class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        m = len(nums)
        i, k = 0, 0

        if m == 0: 
            return k

        while m > 0:
            if nums[i] != val: 
                i += 1
                k += 1
                m -= 1

            elif nums[i] == '_':
                break

            else:
                del nums[i]
                nums.append('_')
                m -= 1

        return k