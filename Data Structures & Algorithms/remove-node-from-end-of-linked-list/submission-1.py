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
        prevNodePos = totalNodes - n # position of node before the one we've to remove
        if prevNodePos == 0: return head.next # remove the head node when n is no. of nodes in linked list
        curr, i = head, 1
        while i != prevNodePos:
            i += 1
            curr = curr.next
        # now curr points to node just before the one we've to remove
        nthNode = curr.next
        curr.next = curr.next.next
        del nthNode # remove the nth node from last (tho its fine to not write this line since we've already linked its previous node to the node after this)
        return head