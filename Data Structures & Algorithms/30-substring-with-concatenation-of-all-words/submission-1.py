class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Time complexity: Loop over the words in s O(k)
        # Space complexity: Create hash maps and word strings with worst case O(n)
        # n is number of characters in s, k is number of words in s or words
        output = []
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1

        stringLength = len(s)
        wordLength = len(words[0])
        windowLength = wordLength * len(words)
        start = 0
        hash_map = {}
        for i in range(stringLength - wordLength + 1)[::wordLength]:
            new_word = s[i : i+wordLength]
            hash_map[new_word] = hash_map.get(new_word, 0) + 1

            if hash_map == freq_map: 
                output.append(start)

            if i // wordLength >= len(words) - 1:
                first_word = s[start : start + wordLength]
                hash_map[first_word] -= 1
                if hash_map[first_word] == 0:
                    del hash_map[first_word]
                start += wordLength

        return output