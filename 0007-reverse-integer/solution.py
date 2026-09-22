class Solution:
    def reverse(self, x: int) -> int:
        # Python handles modulo with negative numbers differently than C/Java.
        # To avoid bugs, we work with the absolute value and re-apply the sign later.
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        res = 0
        # The maximum 32-bit integer is 2,147,483,647. 
        # The limit before multiplying by 10 is 214,748,364.
        max_limit = (2**31 - 1) // 10
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Simulate the 32-bit overflow check strictly before it happens
            if res > max_limit:
                return 0
                
            res = res * 10 + pop
            
        return sign * res
