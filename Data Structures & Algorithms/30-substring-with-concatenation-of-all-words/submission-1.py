
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Time complexity: O(n * L) accounting for string slicing
        # Space complexity: O(k * L) for the frequency maps
        # n is len(s), k is len(words), L is len(words[0])
        output = []
        freq_map = {}
        for word in words:
            freq_map[word] = freq_map.get(word, 0) + 1

        stringLength = len(s)
        wordLength = len(words[0])
        windowLength = wordLength * len(words)

        if stringLength < windowLength: return output

        # Check every possible starting offset
        for offset in range(wordLength):
            start = offset
            hash_map = {}
            count = 0

            for i in range(offset, stringLength - wordLength + 1, wordLength):
                new_word = s[i:i + wordLength]

                # Reset window if word is invalid
                if new_word not in freq_map:
                    hash_map = {}
                    count = 0
                    start = i + wordLength
                    continue

                hash_map[new_word] = hash_map.get(new_word, 0) + 1
                count += 1

                # Shrink window if a word occurs too many times
                while hash_map[new_word] > freq_map[new_word]:
                    first_word = s[start:start + wordLength]
                    hash_map[first_word] -= 1
                    if hash_map[first_word] == 0:
                        del hash_map[first_word]
                    start += wordLength
                    count -= 1

                # Record a complete valid window
                if count == len(words):
                    output.append(start)

                    first_word = s[start:start + wordLength]
                    hash_map[first_word] -= 1
                    if hash_map[first_word] == 0:
                        del hash_map[first_word]
                    start += wordLength
                    count -= 1

        return output
