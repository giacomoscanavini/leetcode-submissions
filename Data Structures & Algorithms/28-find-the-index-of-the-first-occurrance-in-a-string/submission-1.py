class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time complexity: Loop over haystack O(n)
        # Space complexity: Create substring with worst case O(n)
        n = len(needle)
        for i in range(len(haystack) - n + 1): 
            if haystack[i : i + n] == needle[:]:
                return i

        return -1