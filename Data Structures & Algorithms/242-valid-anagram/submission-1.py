class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time complexity: Loop over string O(n)
        # Space complexity: Create hashmap O(n)
        # n is len(s)
        if len(s) != len(t): return False

        hashmap = {}
        for c in s: hashmap[c] = hashmap.get(c, 0) + 1
        for c in t: 
            if c not in hashmap.keys(): return False
            hashmap[c] -= 1
            
        for key,val in hashmap.items():
            if val != 0: return False

        return True