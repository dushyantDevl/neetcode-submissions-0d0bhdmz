# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # base case or smallest problem (either none or one node)
            return head
        
        newHead = self.reverseList(head.next) # goes to last node to make that new head (using base case)
        head.next.next = head # head.next.next represent the front node of the reversed linked list (reversed by recursion, which was pointing to null in some mid recursion step) 
        head.next = None # since head is now a tail node link its next to NULL

        return newHead