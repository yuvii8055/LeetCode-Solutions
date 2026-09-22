class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] represents whether s[0...i-1] matches p[0...j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: Empty string can match patterns like "a*", "a*b*", etc.
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # Case 1: Exact character match or '.' wildcard
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # Case 2: '*' wildcard
                elif p[j - 1] == '*':
                    # Scenario A: Zero occurrences of the preceding character
                    # We drop the '*' and the character before it (move back 2 in pattern)
                    dp[i][j] = dp[i][j - 2]
                    
                    # Scenario B: One or more occurrences
                    # The character before '*' must match the current string character (or be '.')
                    # If so, we consume one character from the string but keep the '*' in the pattern
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
