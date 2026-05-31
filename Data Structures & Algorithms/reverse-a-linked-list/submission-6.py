# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node -> already reversed
        if not head or not head.next:
            return head
        
        # Recurse: reverse everything after head
        new_head = self.reverseList(head.next)

        # Fix the connection:
        # head.next is currently the TAIL of the reversed sublist
        # Make it point back to head
        head.next.next = head
        head.next = None          # head is now the new tail

        return new_head           # bubble up the new head all the way