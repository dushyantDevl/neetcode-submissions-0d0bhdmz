# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # in case of even number of nodes, fast pointer will run upto last node
        # so (fast.next = NULL) and in case of odd number of nodes, fast pointer will run upto node
        # after last i.e. NULL that's why we're checking for `fast==NULL` as well
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # fast moves with twice (2x) the speed of slow towards slow (in a cycle) and slow goes 
            # away from fast by x. so net is 1 only (2x-x) therfore fast is bound to meet slow
            # while going in cycle since the distance between fast and slow will decrease by 1 unit everytime
            # if there's a cycle fast will meet slow pointer in around N-steps -> O(N)
            if fast == slow:
                return True
        
        return False