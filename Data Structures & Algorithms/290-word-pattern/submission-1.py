class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Time complexity: Loop over pattern and s O(n)
        # Space complexity: Create hashmaps O(n)
        # n is len(s) > len(pattern)
        s = s.split(' ')
        if len(pattern) != len(s): return False

        pattern_map = {}
        s_map = {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_map.keys() and pattern_map[pattern[i]] != s[i]: return False
            if s[i] in s_map.keys() and s_map[s[i]] != pattern[i]: return False
            pattern_map[pattern[i]] = s[i]
            s_map[s[i]] = pattern[i]

        return True