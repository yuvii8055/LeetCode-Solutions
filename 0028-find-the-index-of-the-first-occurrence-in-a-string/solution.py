class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        # Optimization: We only need to iterate up to the point where the 
        # remaining characters in haystack are at least as long as the needle.
        for i in range(n - m + 1):
            # Extract a substring of length 'm' and compare it to the needle
            if haystack[i:i + m] == needle:
                return i
                
        return -1
