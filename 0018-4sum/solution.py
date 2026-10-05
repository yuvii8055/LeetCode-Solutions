class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Early Pruning 1: If the 4 smallest numbers are too big, stop entirely.
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Early Pruning 2: If the current number + the 3 largest numbers are too small, skip to next i.
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Early Pruning 3: If the current two numbers + the 2 smallest remaining are too big, break out of j loop.
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Early Pruning 4: If the current two numbers + the 2 largest remaining are too small, skip to next j.
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                    
                # Set up two pointers for the remaining portion of the array
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        # Move both pointers inward to look for other potential pairs
                        left += 1
                        right -= 1
                        
        return result
