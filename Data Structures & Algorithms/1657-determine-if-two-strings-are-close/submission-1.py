class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        hash_map1 = {}
        for ch in word1:
            hash_map1[ch] = hash_map1.get(ch, 0) + 1

        hash_map2 = {}
        for ch in word2:
            hash_map2[ch] = hash_map2.get(ch, 0) + 1

        return (
            hash_map1.keys() == hash_map2.keys()
            and sorted(hash_map1.values()) == sorted(hash_map2.values())
        )