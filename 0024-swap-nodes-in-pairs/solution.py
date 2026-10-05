# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node to handle the edge case of swapping the first pair 
        # and to keep a reference to the new head of the list.
        dummy = ListNode(0, head)
        prev = dummy
        
        # We need at least two nodes ahead of 'prev' to perform a swap
        while prev.next and prev.next.next:
            # Identify the two nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Execute the swap by changing the pointers
            first.next = second.next  # 1 points to 3 (or whatever comes after 2)
            second.next = first       # 2 points back to 1
            prev.next = second        # The node before the pair points to 2
            
            # Move the prev pointer forward by two nodes to prepare for the next pair
            prev = first
            
        return dummy.next
        
