class DoublyLL:
    
    def __init__(self, val=-1, prev=None, nxt=None) -> None:
        self.val, self.prev, self.nxt = val, prev, nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.emptySpaces = k
        self.leftDummy = DoublyLL()
        self.rightDummy = DoublyLL(prev=self.leftDummy)
        self.leftDummy.nxt = self.rightDummy

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        # Insert a node before rightDummy 
        newNode = DoublyLL(val=value, prev=self.rightDummy.prev, nxt=self.rightDummy)
        self.rightDummy.prev.nxt = newNode # older node pointing to rightDummy now points to newNode
        self.rightDummy.prev = newNode

        # Decrement the number of available spaces for new nodes
        self.emptySpaces -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.leftDummy.nxt = self.leftDummy.nxt.nxt
        self.leftDummy.nxt.prev = self.leftDummy
        # del self.leftDummy.nxt
        self.emptySpaces += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.leftDummy.nxt.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rightDummy.prev.val
        
    def isEmpty(self) -> bool:
        return self.leftDummy.nxt == self.rightDummy

    def isFull(self) -> bool:
        return self.emptySpaces == 0

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()