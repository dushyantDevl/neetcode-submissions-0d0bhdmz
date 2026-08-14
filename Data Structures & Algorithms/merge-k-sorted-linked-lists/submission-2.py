# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        temp = []
        for head in lists:
            while head:
                temp.append(head.val)
                head = head.next
        
        temp.sort()
        
        def listToLL():
            head = ListNode(val=temp[0])
            tail = head
            for i in range(1, len(temp)):
                tail.next = ListNode(val=temp[i])
                tail = tail.next
            return head

        return listToLL()