class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time complexity: Loop over magazine and ransomNote O(n + m)
        # Space complexity: Create hashmap O(m)
        # m is len(magazine), n is len(randomNote)
        magazine_map = {}
        for c in magazine: 
            magazine_map[c] = magazine_map.get(c, 0) + 1

        for c in ransomNote:
            magazine_map[c] = magazine_map.get(c, 0) - 1
            if magazine_map[c] < 0: return False

        return True