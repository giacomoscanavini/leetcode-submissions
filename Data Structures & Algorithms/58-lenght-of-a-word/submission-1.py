class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Time complexity: Loop over the string with worst case O(n)
        # Space complexity: Fixed number of variables O(1)
        length = 0
        counting = False
        for i in range(len(s))[::-1]:
            if s[i] == ' ':
                if counting == False: pass
                else: break
            else:
                counting = True
                length += 1

        return length