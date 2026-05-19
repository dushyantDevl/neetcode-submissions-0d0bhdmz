"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # original nodes points to new copied one's so that we can track random node otherwise
        # if we try to make the new copied random list by iterating only through next pointer and 
        # creating new copied nodes at that instant then new copied node can't randomly point to a node 
        # which haven't visited while iterating (since it can be far right)
        ogToCopy = {None: None}
        curr = head
        while curr:
            copiedNode = Node(curr.val)
            ogToCopy[curr] = copiedNode
            curr = curr.next
        
        # Now ogToCopy contains new copied node with same value as in original list

        curr = head # point curr back to head

        # linking of copied node using map (since it contains info about original node linking)
        while curr:
            copiedNode = ogToCopy[curr]
            copiedNode.next = ogToCopy[curr.next]
            copiedNode.random = ogToCopy[curr.random]
            curr = curr.next

        return ogToCopy[head]