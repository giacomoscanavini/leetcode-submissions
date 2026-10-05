class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        for c1, c2 in zip(word1, word2):
            word.extend([c1, c2])

        if len(word1) == len(word2): 
            pass
        else:
            if len(word1) > len(word2):
                word += word1[len(word2) : ]
            else:
                word += word2[len(word1) : ]
            
        return "".join(word)

        