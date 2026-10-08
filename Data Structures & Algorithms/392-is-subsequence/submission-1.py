class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True

        i, j = 0, 0
        while j < len(t):
            if s[i] != t[j]: 
                j += 1
            else:
                i += 1
                j += 1
                 
            if i == len(s): return True

        return False
