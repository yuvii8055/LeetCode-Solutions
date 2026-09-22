class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a mapping of all base and subtractive symbols in descending order
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        
        result = []
        
        for value, symbol in value_symbols:
            # If our number is empty, we can stop checking
            if num == 0:
                break
                
            # See how many times the largest value fits into the remaining number
            count = num // value
            if count > 0:
                result.append(symbol * count)
                # Subtract that total value from the number
                num -= value * count
                
        return "".join(result)
