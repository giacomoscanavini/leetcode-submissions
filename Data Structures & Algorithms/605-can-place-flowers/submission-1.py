class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0: return True

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] + flowerbed[i] + flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1

        return n <= 0 