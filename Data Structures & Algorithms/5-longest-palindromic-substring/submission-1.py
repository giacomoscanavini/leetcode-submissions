class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time complexity: Loop over characters of s and inner loop O(n^2)
        # Space complexity: Create output string worst case O(n)
        # n = len(s)

        n = len(s)
        if n == 1: return s

        maxSub = ''
        for i in range(n):
            # Consider center of a odd-length palindrome
            l, r = i, i
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1 : r]) > len(maxSub): maxSub = s[l+1 : r]

            # Consider center of a even-length palindrome
            l, r = i, i+1
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                l -= 1
                r += 1
            if len(s[l+1 : r]) > len(maxSub): maxSub = s[l+1 : r]

        return maxSub