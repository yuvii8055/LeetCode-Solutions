class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # The height of our container is limited by the shorter line
            current_height = min(height[left], height[right])
            # The width is the distance between the two lines
            current_width = right - left
            
            # Calculate the area and update max_area if it's larger
            current_area = current_height * current_width
            max_area = max(max_area, current_area)
            
            # To maximize area, we must keep the taller line and move the shorter one
            # inward, hoping to find a taller line to compensate for the lost width.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
