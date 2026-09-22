class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_index_map = {}
        max_length = 0
        left = 0 # Left pointer for our sliding window
        
        for right, char in enumerate(s):
            # If the character is already in our dictionary and its last seen 
            # index is at or after our 'left' pointer, we have a duplicate inside our window.
            if char in char_index_map and char_index_map[char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_index_map[char] + 1
            
            # Update the most recent index of the current character
            char_index_map[char] = right
            
            # Calculate current window length and update max_length if it's the largest so far
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            
        return max_length
