# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        temp = []
        for head in lists:
            currListHead = head
            while currListHead:
                temp.append(currListHead.val)
                currListHead = currListHead.next
        temp.sort()
        return self.listToLL(temp)
    
    def listToLL(self, arr):
        head = ListNode(val=arr[0])
        tail = head
        for i in range(1, len(arr)):
            tail.next = ListNode(val=arr[i])
            tail = tail.next
        return head
        