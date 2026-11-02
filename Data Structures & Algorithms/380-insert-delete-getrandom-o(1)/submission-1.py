class RandomizedSet(object):
    def __init__(self):
        # Time complexity: All operations are O(1)
        # Space complexity: Create array and hash map up to O(n)
        self.arr = []
        self.hash_map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.hash_map.keys(): return False
        else:
            self.arr.append(val)
            idx = len(self.arr) - 1
            self.hash_map[val] = idx
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map.keys(): return False
        else:
            idx = self.hash_map[val]
            last_idx = len(self.arr) - 1
            if idx < last_idx:
                self.arr[idx], self.arr[last_idx] = self.arr[last_idx], self.arr[idx]
                self.hash_map[self.arr[idx]] = idx

            self.arr.pop(-1)
            del self.hash_map[val]
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()