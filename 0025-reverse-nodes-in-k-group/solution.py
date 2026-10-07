# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Check if there are at least k nodes left to reverse
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
            
        # Step 2: If we have exactly k nodes, we can proceed with reversal
        if count == k:
            # Recursively call the function for the remainder of the list.
            # 'curr' is currently sitting at node k+1.
            reversed_remainder = self.reverseKGroup(curr, k)
            
            # Step 3: Reverse the current group of k nodes.
            # Instead of pointing the end of our reversed list to None, 
            # we point it directly to the result of our recursive call.
            curr_node = head
            prev_node = reversed_remainder 
            
            for _ in range(k):
                temp = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp
                
            # prev_node is the new head of this reversed k-group
            return prev_node
            
        # If we have fewer than k nodes left, return the head exactly as it is (no reversal)
        return head
