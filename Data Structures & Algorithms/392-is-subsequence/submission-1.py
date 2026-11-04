class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Time complexity: Loop over the string O(n)
        # Space complexity: Fixed number of variables O(1)
        if len(s) == 0: return True
        if len(s) > len(t): return False
        
        j = 0
        for i in range(len(t)):
            if t[i] == s[j]: j += 1
            if j > len(s)-1: return True

        return False