class NodeList:
    def __init__(self, key=-1, val=-1, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashMap = [NodeList() for i in range(10**4)]

    def hash(self, key):
        return key % len(self.hashMap)

    def put(self, key: int, value: int) -> None:
        curr = self.hashMap[self.hash(key)]
        while curr.next:
            if curr.next.key == key: # since 1st one dummy node in the list we've to use curr.next
                curr.next.val = value
                return
            curr = curr.next
        curr.next = NodeList(key,value)

    def get(self, key: int) -> int:
        curr = self.hashMap[self.hash(key)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashMap[self.hash(key)]
        while curr and curr.next:
            if curr.next.key==key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)