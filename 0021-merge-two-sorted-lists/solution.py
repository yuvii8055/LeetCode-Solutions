# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy node acts as the starting point for our merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists as long as neither is empty
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                
            # Move the pointer of the merged list forward
            current = current.next
            
        # If one list is exhausted but the other still has nodes, 
        # append the remaining nodes directly to the merged list.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # dummy.next points to the actual head of our merged list
        return dummy.next
