class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Time complexity: Sorting and looping over the array O(n logn)
        # Space complexity: Creating sorted array O(n)
        citations.sort(reverse=True)
        h = 0
        for cit in citations:
            if cit > h: h += 1
            else:
                break

        return h