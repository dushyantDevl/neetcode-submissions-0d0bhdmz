# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack, temp = [], head
        # store all the values of linked list in stack
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head
        '''
        pop values from stack to make new linked list since stack top contains values of original 
        linked list starting from last
        '''
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        
        return head