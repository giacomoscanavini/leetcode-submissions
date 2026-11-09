class Solution:
    def isHappy(self, n: int) -> bool:
        # Note that: A number is converted to at most log10(n) digits 
        #    and the cycle either ends at 1 or repeats after a constant number of steps
        # Time complexity: O(log10(n))
        # Space complexity: Create set of fixed number of states O(1)
        # n is order of magnitude of input number
        states = set()

        while n != 1:
            if n in states: return False

            states.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return True
