class Node:
    def __init__(self, key=-1, val=-1, freq=0, prev=None, nxt=None) -> None:
        self.key, self.val, self.freq = key, val, freq
        self.prev, self.nxt = prev, nxt


class DoublyLL:
    def __init__(self) -> None:
        self.dummyHead = Node()
        self.dummyTail = Node(prev=self.dummyHead)
        self.dummyHead.nxt = self.dummyTail
        self.size = 0

    def insertAtHead(self, node: Node):
        node.prev = self.dummyHead
        node.nxt = self.dummyHead.nxt
        self.dummyHead.nxt.prev = node
        self.dummyHead.nxt = node

        self.size += 1
    
    def removeLinks(self, node:Node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.keyToNode = {}
        self.freqToNodes = {}
        self.minFreq = self.currSize = 0

    def _updateFreqListMap(self, node: Node):
        del self.keyToNode[node.key]
        # remove the node from the lower frequency list (before moving to higher frequency list)
        # list can be accessed from the given node's frequency
        self.freqToNodes[node.freq].removeLinks(node)

        # Update the min freq if the list containing the `node` doesn't contain any nodes anymore
        if node.freq == self.minFreq and self.freqToNodes[node.freq].size == 0:
            self.minFreq += 1 

        higherFreqList = DoublyLL()
        if (node.freq + 1) in self.freqToNodes:
            higherFreqList = self.freqToNodes[node.freq + 1]
        
        node.freq += 1
        higherFreqList.insertAtHead(node) # insert this recently accessed node at head (indicating its used recently)
        # update the original freq to nodes map, by updating the changes made in particular frequency list
        self.freqToNodes[node.freq] = higherFreqList
        self.keyToNode[node.key] = node # update the map again after making above changes

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            self._updateFreqListMap(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self._updateFreqListMap(node)
        else:
            if self.currSize == self.capacity:
                reqdList = self.freqToNodes[self.minFreq]
                # remove the least recently used node (prev of dummyTail)
                del self.keyToNode[reqdList.dummyTail.prev.key]
                self.freqToNodes[self.minFreq].removeLinks(reqdList.dummyTail.prev)
                self.currSize -= 1
            # Now add the new node in the frequency=1 (since its the first time its accessed)
            self.currSize += 1
            self.minFreq = 1

            # Create new frequency list if not present otherwise just make update in the one already exist
            newFreqList = DoublyLL()
            if self.minFreq in self.freqToNodes:
                newFreqList = self.freqToNodes[self.minFreq]

            newNode = Node(key=key,val=value,freq=1)
            newFreqList.insertAtHead(newNode)
            self.keyToNode[key] = newNode
            self.freqToNodes[self.minFreq] = newFreqList


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




    