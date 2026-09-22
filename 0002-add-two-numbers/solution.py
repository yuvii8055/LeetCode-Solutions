# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node to act as the starting point of our new linked list
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Continue looping if there are nodes left in l1, l2, OR if there's a carry left over
        while l1 or l2 or carry:
            # Get the values from the current nodes (use 0 if the list has ended)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = v1 + v2 + carry
            carry = total // 10  # Integer division gets the tens digit (e.g., 15 // 10 = 1)
            
            # Create a new node with the ones digit and attach it to our result list
            current.next = ListNode(total % 10)
            
            # Move all pointers forward
            current = current.next
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
                
        # Return the next node after dummy, which is the actual head of the result
        return dummy.next
