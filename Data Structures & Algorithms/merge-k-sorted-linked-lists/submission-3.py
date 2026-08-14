# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
             return None
        
        ## if node values are equal then by default minHeap will check for next value
        ## in the tuple so to be safe, also push the idx of the head from lists
        ## so that if two head values are equal the head with the lower index will
        ## be push first
        minHeap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(minHeap) # T.C -> O(k)
        
        dummy = ListNode()
        tail = dummy

        ## to keep it consistent, now push new ID for newer push in the minHeap
        ## since we dont have any index for other nodes in the list (i.e. except head
        ## which is stored in lists) and increment it after each push so that when 
        ## popping the node in case of duplicates the lower ID is popped first
        uniqueID = len(lists)

        while minHeap:
            node = heapq.heappop(minHeap)[2]
            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(minHeap, (node.next.val, uniqueID, node.next))
                uniqueID += 1
            
        return dummy.next
