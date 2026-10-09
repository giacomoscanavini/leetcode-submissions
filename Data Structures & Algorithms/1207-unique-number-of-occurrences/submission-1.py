class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash_map = {}
        for value in arr:
            hash_map[value] = hash_map.get(value, 0) + 1

        return len(set(hash_map.values())) == len(hash_map.values())