class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start_idx = 0
        total_fuel = 0
        current_fuel = 0

        for i in range(len(gas)):
            fuel = gas[i] - cost[i]
            total_fuel += fuel
            current_fuel += fuel

            if current_fuel < 0:
                current_fuel = 0
                start_idx = i + 1

        if total_fuel < 0: return -1
        else: return start_idx