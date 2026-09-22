class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647  # 2**31 - 1
        INT_MIN = -2147483648 # -2**31
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # If we reached the end of the string, return 0
        if i == n:
            return 0
            
        # 2. Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Convert digits to integer
        res = 0
        while i < n and s[i].isdigit():
            # Build the number by multiplying by 10 and adding the new digit
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply the sign
        res *= sign
        
        # 4. Rounding (Clamp to 32-bit signed integer range)
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
            
        return res
