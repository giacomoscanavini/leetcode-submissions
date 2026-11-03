class Solution:
    def intToRoman(self, num: int) -> str:
        # Time complexity: Fixed number of operations O(1)
        # Space complexity: Fixed number of variables O(1)
        roman = '' 
        mill = num // 1000
        roman += 'M' * mill

        remaining = num - mill * 1000
        cent = remaining // 100
        if cent: 
            if cent <= 3: roman += 'C' * cent
            elif cent == 4: roman += 'CD'
            elif 5 <= cent <= 8: roman = roman + 'D' + 'C' * (cent - 5)
            else: roman += 'CM'

        remaining = remaining - cent * 100
        deci = remaining // 10
        if deci: 
            if deci <= 3: roman += 'X' * deci
            elif deci == 4: roman += 'XL'
            elif 5 <= deci <= 8: roman = roman + 'L' + 'X' * (deci - 5)
            else: roman += 'XC'

        remaining = remaining - deci * 10
        unit = remaining
        if unit: 
            if unit <= 3: roman += 'I' * unit
            elif unit == 4: roman += 'IV'
            elif 5 <= unit <= 8: roman = roman + 'V' + 'I' * (unit - 5)
            else: roman += 'IX'

        return roman