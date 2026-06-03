# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwoSortedList(head, lists[i])
        return head

    def mergeTwoSortedList(self, l1, l2):
        head = ListNode()
        dummy = head
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2

        return head.next