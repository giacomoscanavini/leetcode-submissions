class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Time complexity: Loop over strings and loop over each character O(m * n)
        # Space complexity: Create output array O(m * n)
        # n is len(string), m is len(strs)
        anagrams = {}
        for string in strs:
            tuple_key = [0] * 26
            for c in string:
                idx = 'abcdefghijklmnopqrstuvwxyz'.index(c)
                tuple_key[idx] += 1
            tuple_key = tuple(tuple_key)

            if anagrams.get(tuple_key, 0): anagrams[tuple_key].append(string)
            else: anagrams[tuple_key] = [string]

        return list(anagrams.values())