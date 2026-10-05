class Solution:
    def candy(self, ratings: list[int]) -> int:
        if len(ratings) == 1:
            return 1
        
        left = [0] * len(ratings)
        right = [0] * len(ratings)
        candies_left = [1] * len(left)
        candies_right = [1] * len(right)

        for i in range(1, len(ratings)):
            j = len(ratings) - i - 1
            left[i] = ratings[i-1] - ratings[i]
            right[j] = ratings[j+1] - ratings[j]

            if left[i] < 0: 
                candies_left[i] = candies_left[i-1] + 1

            if right[j] < 0: 
                candies_right[j] = candies_right[j+1] + 1

        for i in range(len(ratings)):
            candies_left[i] = max(candies_left[i], candies_right[i])

        return sum(candies_left)