# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeFreq = {}
        while head:
            nodeFreq[head] = nodeFreq.get(head, 0) + 1
            if nodeFreq[head] > 1: return True
            head = head.next
        return False