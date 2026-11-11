class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Time complexity: Loop over character of s, loop over each word in wordDict O(n * k)
        # Space complexity: Create dp array O(n)
        # n is len(s), k is len(wordDict)

        # Create array of states
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s))[::-1]:
            # For each character we check if a word from the dictionary starts there
            ans = False
            for w in wordDict:
                if s[i : i + len(w)] == w:
                    # If a word matches we check if it connects to a previous found word starting point
                    ans = ans or dp[i + len(w)]

            # We update the array of states if we found a connection to a next state
            dp[i] = 1 if ans == True else 0

        # If the chain connects all the way we return True
        if dp[0] == True: return True
        else: return False