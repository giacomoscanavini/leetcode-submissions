class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity: Loop over the string O(n)
        # Space complexity: Fixed number of variables O(1)
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] == ' ' or not s[l].lower().isalnum(): l += 1
            elif s[r] == ' ' or not s[r].lower().isalnum(): r -= 1
            else:
                if s[l].lower() == s[r].lower(): 
                    l += 1
                    r -= 1
                else:
                    return False

        return True