class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time complexity: Loop over s O(n) 
        # Space complexity: Create hash map with worst case O(n)
        currentSub = {}
        maxLength = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in currentSub.keys():
                l = max(l, currentSub[c] + 1)
                
            currentSub[c] = r
            maxLength = max(maxLength, r-l+1)

        return maxLength