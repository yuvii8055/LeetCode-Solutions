class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer limits
        INT_MAX = (1 << 31) - 1  # 2147483647
        INT_MIN = -(1 << 31)     # -2147483648
        
        # Handle the single mathematically possible overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        # Determine the sign of the result
        # If one is negative and the other is positive, the result is negative
        is_negative = (dividend < 0) != (divisor < 0)
        
        # Work strictly with positive numbers to make logic easier
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # Iterate from the largest possible power of 2 down to 0
        for i in range(31, -1, -1):
            # (abs_divisor << i) is the same as: abs_divisor * (2 ** i)
            # We check if this massive chunk can fit inside our remaining dividend
            if (abs_divisor << i) <= abs_dividend:
                # Subtract the massive chunk from our dividend
                abs_dividend -= (abs_divisor << i)
                # Add the multiple (2^i) to our quotient count
                quotient += (1 << i)
                
        # Apply the correct sign
        if is_negative:
            quotient = -quotient
            
        # Clamp the result strictly within 32-bit bounds (as requested)
        return min(max(INT_MIN, quotient), INT_MAX)
