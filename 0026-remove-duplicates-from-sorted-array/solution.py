class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # The first element is always unique. 
        # We start looking for where to place the next unique element at index 1.
        insert_index = 1
        
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's a new unique number.
            if nums[i] != nums[i - 1]:
                # Place it at the insert_index, then increment the insert_index.
                nums[insert_index] = nums[i]
                insert_index += 1
                
        return insert_index
