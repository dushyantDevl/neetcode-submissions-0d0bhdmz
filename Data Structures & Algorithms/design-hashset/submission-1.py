class MyHashSet:

    def __init__(self):
        self.myHash = set()

    def add(self, key: int) -> None:
        self.myHash.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.myHash.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.myHash else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)