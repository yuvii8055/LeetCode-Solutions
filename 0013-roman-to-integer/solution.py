class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping each Roman numeral to its integer value
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current symbol is less than the next symbol, it's a subtractive case
            if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                total -= roman_values[s[i]]
            # Otherwise, it's a standard additive case
            else:
                total += roman_values[s[i]]
                
        return total
