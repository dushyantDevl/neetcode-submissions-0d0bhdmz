# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(val=-1, next=head) # keep track of head and edge cases

        # Find the left node and the node before it
        leftPrev, curr = dummyNode, head
        for _ in range(left-1):
            leftPrev, curr = curr, curr.next

        # Now leftPrev points to node before left and curr points to left node
        prev = leftPrev
        # Reverse the nodes links between left and right (inclusive)
        for _ in range(right - left + 1):
            tempCurrNext = curr.next
            curr.next = prev
            prev, curr = curr, tempCurrNext
        
        # Now updates the links of extreme end nodes of the newly reversed linkedList (from left to right)
        leftPrev.next.next = curr # points the left node (before reversing) to the node after new right node (after reversing)
        leftPrev.next = prev # points to the node before left to the node right node (which is reversed now i.e on older left position)

        return dummyNode.next


