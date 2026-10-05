class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(' ')
        s = [x for x in s if x != '']
        s.reverse()
        return " ".join(s)