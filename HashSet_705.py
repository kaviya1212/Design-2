class MyHashSet:

    # time complexity: o(1)
    # space complexity: o(n)
    # Used fixed array where all elements are set to None. 
    # When a key is added, the value at the corresponding index is set to True to indicate the key exists. 
    # To remove a key, the value at that index is reset to None. To check if a key exists, the value at the index is checked—if it's True, the key is present; otherwise, it's absent.

    def __init__(self):
        self.hashset = [None] * 10000000

    def add(self, key: int) -> None:
        self.hashset[key] = True  

    def remove(self, key: int) -> None:
        self.hashset[key] = None  

    def contains(self, key: int) -> bool:
        return self.hashset[key] is not None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)