class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # This pointer tracks where the next valid (non-val) element should be placed
        insert_index = 0
        
        for i in range(len(nums)):
            # If we find a number that is NOT the value we want to remove
            if nums[i] != val:
                # Place it at the front of the array using our insert_index
                nums[insert_index] = nums[i]
                insert_index += 1
                
        return insert_index
