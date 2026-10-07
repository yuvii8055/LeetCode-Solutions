class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper function to find either the left or right boundary
        def findBound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    # If we are looking for the first occurrence, keep searching left
                    if is_first:
                        right = mid - 1
                    # If we are looking for the last occurrence, keep searching right
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound
            
        # Find the first occurrence
        first_pos = findBound(True)
        
        # If the target isn't in the array at all, return early
        if first_pos == -1:
            return [-1, -1]
            
        # Find the last occurrence
        last_pos = findBound(False)
        
        return [first_pos, last_pos]
