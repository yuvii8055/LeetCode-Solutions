class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Target found, return its exact index
            if nums[mid] == target:
                return mid
                
            # If the middle element is smaller than the target, 
            # the target must be in the right half.
            elif nums[mid] < target:
                left = mid + 1
                
            # If the middle element is larger, 
            # the target must be in the left half.
            else:
                right = mid - 1
                
        # If the loop finishes and the target wasn't found, 
        # the 'left' pointer naturally rests at the exact insertion index.
        return left
