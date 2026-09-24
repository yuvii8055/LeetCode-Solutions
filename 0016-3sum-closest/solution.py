class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        # Initialize with infinity so the first sum automatically becomes the closest
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If this sum is closer to the target than our previous best, update it
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # If the sum is exactly the target, we can't get any closer!
                if current_sum == target:
                    return current_sum
                    
                # If the sum is too small, move the left pointer to a larger number
                elif current_sum < target:
                    left += 1
                    
                # If the sum is too large, move the right pointer to a smaller number
                else:
                    right -= 1
                    
        return closest_sum
        
