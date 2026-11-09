class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # Time complexity: Loop over nums O(n)
        # Space complexity: Create set of numbers O(k)
        # k is window length, n is len(nums)
        if k == 0: return False

        current_window = set()
        for i in range(len(nums)):
            if i <= k: 
                if nums[i] in current_window: return True
            else:
                first_idx = i-k-1
                current_window.remove(nums[first_idx])
                if nums[i] in current_window: return True

            current_window.add(nums[i])

        return False