class Solution:
    def candy(self, ratings: list[int]) -> int:
        # Time complexity: Loop over ratings O(n)
        # Space complexity: Create left and right arrays O(n)
        left_candy = [1] * len(ratings)
        right_candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: left_candy[i] = left_candy[i-1] + 1
            else: pass

        for j in range(len(ratings)-1)[::-1]:
            if ratings[j] > ratings[j+1]: right_candy[j] = right_candy[j+1] + 1
            else: pass

        minCandy = 0
        for i in range(len(ratings)):
            minCandy += max(left_candy[i], right_candy[i])

        return minCandy