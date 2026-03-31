class NodeList:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [NodeList(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        curr = self.set[index]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = NodeList(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = key % len(self.set)
            curr = self.set[index]
            while curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return
                curr = curr.next 

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        curr = self.set[index]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)