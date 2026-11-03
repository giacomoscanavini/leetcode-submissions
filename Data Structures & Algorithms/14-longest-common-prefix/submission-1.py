class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Time complexity: Loop over common character and strings O(m * n)
        # Space complexity: Create common string O(m)
        if len(strs) == 1: return strs[0]

        minL = min([len(s) for s in strs])
        if minL == 0: return ''

        common = ''
        for i in range(minL):
            c = strs[0][i]
            for string in strs[1:]:
                if string[i] == c: pass
                else: 
                    return common
            common += c

        return common