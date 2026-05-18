# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, totalNodes = head, 0
        while curr:
            totalNodes += 1
            curr = curr.next
        prevNodePos = totalNodes - n
        if prevNodePos == 0: return head.next
        curr, i = head, 1
        while i != prevNodePos:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
        
        
        