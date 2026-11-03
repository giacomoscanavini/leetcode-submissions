class Solution:
    def romanToInt(self, s: str) -> int:
        # Time complexity: Loop over the string O(n)
        # Space complexity: Fixed number of variables O(1)
        total = 0
        previous = 0
        for i in range(len(s))[::-1]:
            if s[i] == 'I': value = 1
            elif s[i] == 'V': value = 5
            elif s[i] == 'X': value = 10
            elif s[i] == 'L': value = 50
            elif s[i] == 'C': value = 100
            elif s[i] == 'D': value = 500
            else: value = 1000

            if value < previous: total -= value
            else: total += value
            previous = value

        return total