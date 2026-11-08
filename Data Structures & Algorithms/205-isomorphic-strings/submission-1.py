class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Time complexity: Loop over s and t O(n + m)
        # Space complexity: Create arrays O(n + m)
        # n is len(s), m is len(t)
        s_map = []
        t_map = []
        for c in s: s_map.append(s.index(c))
        for c in t: t_map.append(t.index(c))

        if s_map == t_map: return True
        else: return False