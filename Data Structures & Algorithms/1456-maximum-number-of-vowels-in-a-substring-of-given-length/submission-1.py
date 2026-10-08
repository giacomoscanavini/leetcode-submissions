class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        currCounter = sum([1 for x in s[: k] if x in vowels])
        maxCounter = currCounter
        
        for i in range(k, len(s)):
            if s[i-k] in vowels: currCounter -= 1
            if s[i] in vowels: currCounter += 1
            maxCounter = max(maxCounter, currCounter)

        return maxCounter