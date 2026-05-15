# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        bridge, temp = [], head
        # store all the values of linked list in bridge list
        while temp:
            bridge.append(temp.val)
            temp = temp.next
        
        n = len(bridge)
        # reverse the bridge list
        for i in range(n//2):
            bridge[i], bridge[n-i-1] = bridge[n-i-1], bridge[i]
        
        temp, i = head, 0
        # copy values from reversed bridge list to linked list (starting from head to tail)
        while temp:
            temp.val = bridge[i]
            temp = temp.next
            i += 1
        
        return head