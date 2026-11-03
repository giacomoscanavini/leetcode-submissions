class Solution:
    def reverseWords(self, s: str) -> str:
        # Time complexity: Loop over the characters and the words O(n)
        # Space complexity: Create list of words and final string O(n)
        s = s.strip().split(" ")
        s = [x for x in s if len(x) > 0]
        l, r = 0, len(s)-1
        while l < r: 
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return " ".join(s)