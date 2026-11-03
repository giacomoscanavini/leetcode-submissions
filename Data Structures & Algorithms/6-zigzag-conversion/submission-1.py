class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Time complexity: Loop over characters of string O(n)
        # Space complexity: Create new string O(n)
        if numRows == 1: return s

        final_string = ['' for x in range(numRows)]
        reverse = False
        at = 0
        for i in range(len(s)):
            final_string[at] += s[i]
            if not reverse: 
                if at == numRows - 1: 
                    reverse = True
                    at -= 1
                else: 
                    at += 1
            else: 
                if at == 0: 
                    reverse = False
                    at += 1
                else:
                    at -= 1

        return "".join(final_string)