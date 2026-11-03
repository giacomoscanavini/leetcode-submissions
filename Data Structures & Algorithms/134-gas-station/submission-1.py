class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Time complexity: Loop over the gas stations O(n)
        # Space complexity: Fixed number of variables O(1)
        start = 0
        available_gas = 0
        total_gas = 0
        for i,(g,c) in enumerate(zip(gas, cost)):
            available_gas += (g - c)
            total_gas += (g - c)
            if available_gas < 0:
                available_gas = 0
                start = i + 1 

        if total_gas >= 0: 
            return start
        else:
            return -1