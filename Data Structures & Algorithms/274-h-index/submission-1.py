class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if len(citations) == 1: 
            if citations[0] == 0: return 0
            else: return 1

        citations = sorted(citations, reverse=True)
        h = 0
        for i,cit in enumerate(citations):
            if cit >= i+1:
                h += 1
            else:
                break

        return h 
            

        