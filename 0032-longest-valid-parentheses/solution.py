class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        
        # Pass 1: Left to Right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                # We found a perfectly balanced substring
                max_length = max(max_length, 2 * right)
            elif right > left:
                # The substring is irreparably broken (too many closing brackets)
                # Reset counters to start fresh on the next character
                left = 0
                right = 0
                
        # Reset counters for the reverse pass
        left = 0
        right = 0
        
        # Pass 2: Right to Left
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1
                
            if left == right:
                # We found a perfectly balanced substring
                max_length = max(max_length, 2 * left)
            elif left > right:
                # The substring is irreparably broken (too many opening brackets)
                left = 0
                right = 0
                
        return max_length
