# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr, temp = [], head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        n = len(arr)
        
        for i in range(0, n, k):
            if i+k-1 < n:
                self.reverseList(i, i+k-1, arr)

        head = ListNode(val=arr[0])
        tail = head

        for i in range(1, n):
            tail.next = ListNode(val=arr[i])
            tail = tail.next
        
        return head

    def reverseList(self, l, r, arr):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1