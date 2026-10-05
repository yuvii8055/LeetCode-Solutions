# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to the head.
        # This simplifies edge cases, like when we need to remove the very first node.
        dummy = ListNode(0, head)
        
        slow = dummy
        fast = dummy
        
        # Step 1: Move the fast pointer 'n' steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Step 2: Move both pointers at the same speed until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # Step 3: 'slow' is now pointing to the node exactly BEFORE the one we want to delete.
        # We skip the target node by pointing to the node after it.
        slow.next = slow.next.next
        
        # Return the actual head of the list (dummy.next)
        return dummy.next
