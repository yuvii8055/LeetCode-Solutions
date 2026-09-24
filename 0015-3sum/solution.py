class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily use the two-pointer technique and skip duplicates
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # If the current number is greater than 0, the sum can never equal 0 
            # because the array is sorted and all remaining numbers are also positive.
            if nums[i] > 0:
                break
                
            # Set up two pointers for the remaining portion of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # We need a larger sum, move the left pointer to a larger number
                    left += 1
                elif total > 0:
                    # We need a smaller sum, move the right pointer to a smaller number
                    right -= 1
                else:
                    # We found a valid triplet!
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements for the second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    # Skip duplicate elements for the third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward to look for other potential pairs
                    left += 1
                    right -= 1
                    
        return result
