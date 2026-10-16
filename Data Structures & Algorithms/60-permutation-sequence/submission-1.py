class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        
        def factorial(x):
            if x - 1 > 0: return x * factorial(x - 1)
            else: return 1

        values_per_block = factorial(n) // n
        k -= 1

        output = []
        while nums:
            output.append(str(nums[k // values_per_block]))
            nums.pop(k // values_per_block)

            if not nums: break

            k = k % values_per_block
            values_per_block = values_per_block // len(nums)

        return "".join(output)