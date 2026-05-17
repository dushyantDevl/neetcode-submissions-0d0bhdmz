# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, nodesList = head, []
        # store all the nodes in list in given order
        while curr:
            nodesList.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodesList)-1
        while i < j: # link from 1st node of left halve to last node of right halve then move i and j closer
            nodesList[i].next = nodesList[j]
            i += 1

            if i >= j: break # make sure i didn't go past j since we're incrementing it first

            nodesList[j].next = nodesList[i]
            j -= 1
        
        nodesList[i].next = None