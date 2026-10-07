class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars) <= 1: return len(chars)

        i = 1
        counter = 1
        while i < len(chars):
            if chars[i] == chars[i - 1]:
                counter += 1
                chars.pop(i)
            else:
                if counter > 1:
                    digits = str(counter)

                    for offset, digit in enumerate(digits):
                        chars.insert(i + offset, digit)

                    i += 1 + len(digits)
                    counter = 1

                else:
                    i += 1

        if counter > 1:
            chars.extend(str(counter))

        return len(chars)