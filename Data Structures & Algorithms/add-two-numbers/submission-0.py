# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(-1), 0
        curr = dummy
        while l1 or l2:
            sum = carry
            if l1: sum += l1.val
            if l2: sum += l2.val
            
            newNode = ListNode(sum % 10)
            carry   = sum // 10

            curr.next = newNode
            curr      = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry != 0:
            curr.next = ListNode(carry)
        
        return dummy.next

