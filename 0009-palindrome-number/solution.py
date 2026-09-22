class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Step 1: Handle edge cases immediately.
        # Negative numbers are not palindromes (e.g., -121 becomes 121-).
        # Numbers ending in 0 cannot be palindromes unless the number is exactly 0 (e.g., 10 becomes 01).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        
        # Step 2: Reverse the second half of the number.
        # We know we've reached the middle when the remaining 'x' is 
        # less than or equal to our 'reversed_half'.
        while x > reversed_half:
            pop = x % 10
            reversed_half = reversed_half * 10 + pop
            x //= 10
            
        # Step 3: Check for equality.
        # If the length is even, x will exactly equal reversed_half (e.g., 1221 -> x=12, reversed_half=12).
        # If the length is odd, reversed_half will have the middle digit. 
        # We can drop it using reversed_half // 10 (e.g., 12321 -> x=12, reversed_half=123).
        return x == reversed_half or x == reversed_half // 10
