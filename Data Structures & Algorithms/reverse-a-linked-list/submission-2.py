# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next # save this link for iterating forward (since we'll be updating curr.next at each iteration)
            curr.next = prev # link current node's next to previous node (reverse)
            prev = curr # track current node so that we can reverse in next iteration
            curr = temp # move curr to next node in the linked list

        # curr now pointing to NULL       
        return prev # will be pointing to last node in linked list (which is now first or head after reversing)