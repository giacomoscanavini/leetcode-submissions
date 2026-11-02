class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time complexity: Loop over array O(m+n)
        # Space complexity: Replacement happens in place O(1)
        r1, r2, at = m-1, n-1, m+n-1
        while r2 >= 0:
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[at] = nums1[r1]
                r1 -= 1
            else:
                nums1[at] = nums2[r2]
                r2 -= 1
            
            at -= 1