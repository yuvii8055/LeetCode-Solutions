class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Step 1: Cyclic Sort - Place every valid number x at index x - 1
        for i in range(n):
            # We only care about positive integers that can actually fit in our array (1 to n)
            # We keep swapping until the current index holds the correct number or an invalid number
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Find the index where nums[i] actually belongs
                correct_idx = nums[i] - 1
                
                # Swap the numbers to put nums[i] in its rightful place
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Scan the array to find the first missing number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: If all spots are perfectly filled from 1 to n, the missing number is n + 1
        return n + 1
        
