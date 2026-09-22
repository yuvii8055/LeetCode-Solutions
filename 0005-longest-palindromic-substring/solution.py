class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
            
        start, end = 0, 0
        
        # Helper function to expand outwards from a given center
        def expandAroundCenter(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome we found
            return right - left - 1
            
        for i in range(len(s)):
            # Check for odd-length palindromes (center is one character)
            len1 = expandAroundCenter(i, i)
            # Check for even-length palindromes (center is between two characters)
            len2 = expandAroundCenter(i, i + 1)
            
            # Take the longest of the two
            max_len = max(len1, len2)
            
            # If we found a longer palindrome than our current record, update the boundaries
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        # Slice the string using the found boundaries
        return s[start:end+1]
