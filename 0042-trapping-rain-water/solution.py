class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        # Keep track of the maximum height seen from both sides
        left_max = height[left]
        right_max = height[right]
        
        water_trapped = 0
        
        # Move pointers inward until they meet
        while left < right:
            # The water level is determined by the shorter of the two bounding max heights
            if left_max < right_max:
                left += 1
                # Update the max height seen from the left so far
                left_max = max(left_max, height[left])
                # Add any water trapped above the current block
                water_trapped += left_max - height[left]
            else:
                right -= 1
                # Update the max height seen from the right so far
                right_max = max(right_max, height[right])
                # Add any water trapped above the current block
                water_trapped += right_max - height[right]
                
        return water_trapped
