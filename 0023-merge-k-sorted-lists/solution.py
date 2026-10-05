import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # We will use a min-heap to keep track of the smallest current node across all lists
        heap = []
        
        # 1. Initialize the heap with the head of each linked list
        for i, node in enumerate(lists):
            if node:
                # Push a tuple of (value, list_index, node). 
                # The list_index acts as a tie-breaker if two nodes have the same value, 
                # preventing Python from throwing a TypeError for comparing ListNode objects.
                heapq.heappush(heap, (node.val, i, node))
                
        # Dummy node to build our result list
        dummy = ListNode(0)
        current = dummy
        
        # 2. Extract the minimum node and push the next node from that list
        while heap:
            # Pop the smallest node from the heap
            val, i, smallest_node = heapq.heappop(heap)
            
            # Add it to our merged list
            current.next = smallest_node
            current = current.next
            
            # If the extracted node has a next node, push it into the heap
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, i, smallest_node.next))
                
        return dummy.next
