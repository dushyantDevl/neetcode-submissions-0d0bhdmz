# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, cur = 0, head
        while cur:
            cur = cur.next
            n += 1

        n //= 2
        cur = head
        while n:
            n -= 1
            cur = cur.next
        return cur