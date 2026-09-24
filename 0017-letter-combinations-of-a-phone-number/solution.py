class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Base case: if the input is empty, return an empty list immediately
        if not digits:
            return []
            
        # Mapping of digits to letters as seen on a telephone keypad
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        # Backtracking helper function
        def backtrack(index: int, current_string: list[str]):
            # If our current string is the same length as the input digits, 
            # we've formed a complete combination. Add it to our results.
            if index == len(digits):
                result.append("".join(current_string))
                return
                
            # Get the letters that the current digit maps to
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]
            
            # Loop through these letters and build combinations
            for letter in possible_letters:
                current_string.append(letter)         # 1. Choose a letter
                backtrack(index + 1, current_string)  # 2. Explore further digits
                current_string.pop()                  # 3. Un-choose (Backtrack) to try the next letter
                
        # Start the recursion from the first digit (index 0) with an empty list
        backtrack(0, [])
        
        return result
