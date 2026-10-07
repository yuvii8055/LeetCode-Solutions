class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right (the pivot)
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
            
        # Step 2: If we found a valid pivot, find the rightmost element greater than it
        if pivot >= 0:
            successor = n - 1
            while nums[successor] <= nums[pivot]:
                successor -= 1
            
            # Swap the pivot with this successor
            nums[pivot], nums[successor] = nums[successor], nums[pivot]
            
        # Step 3: Reverse the sequence to the right of the pivot
        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
