class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        pairs = []
        potions = sorted(potions, reverse=False)
        nPotions = len(potions)

        for spell in spells:
            i = 0
            j = nPotions - 1
            while i <= j:
                m = i + (j - i) // 2
                product = spell * potions[m]
                if product >= success:
                    j = m - 1
                else:
                    i = m + 1
            
            pairs.append(nPotions - i)

        return pairs