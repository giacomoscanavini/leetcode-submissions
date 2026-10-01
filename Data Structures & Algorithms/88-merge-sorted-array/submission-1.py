class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead
        """
        if m == 0: nums1[0:] = nums2[0:]
        elif n == 0: pass
        else:
            i, j = 0, 0
            while m > 0: 
                if nums1[i] <= nums2[j]:
                    i += 1
                    m -= 1

                else:
                    nums1.insert(i, nums2[j])
                    del nums1[-1]
                    i += 1
                    j += 1

                if j == n: 
                    break

                if m == 0:
                    nums1[i:] = nums2[j:]
                    break