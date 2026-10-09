class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        hash_map1 = {}
        for num in nums1:
            hash_map1[num] = hash_map1.get(num, 0) + 1

        hash_map2 = {}
        for num in nums2:
            hash_map2[num] = hash_map2.get(num, 0) + 1

        list1 = []
        for key in hash_map1.keys():
            if key not in hash_map2.keys(): list1.append(key)
        
        list2 = []
        for key in hash_map2.keys():
            if key not in hash_map1.keys(): list2.append(key)

        return [list1, list2]


"""
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1.difference(set2)), list(set2.difference(set1)]
"""