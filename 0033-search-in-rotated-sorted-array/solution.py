class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # We found the target
            if nums[mid] == target:
                return mid
                
            # Determine which half of the array is perfectly sorted.
            # Case 1: The left half is strictly sorted.
            if nums[left] <= nums[mid]:
                # Check if the target mathematically falls within this sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is here, discard the right half
                else:
                    left = mid + 1   # Target is not here, discard the left half
                    
            # Case 2: The right half must be strictly sorted.
            else:
                # Check if the target mathematically falls within this sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is here, discard the left half
                else:
                    right = mid - 1  # Target is not here, discard the right half
                    
        return -1
