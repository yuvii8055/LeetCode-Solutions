class Solution:
    def isValid(self, s: str) -> bool:
        # A stack to keep track of opening brackets
        stack = []
        
        # Hash map for keeping track of mappings. 
        # This makes the code cleaner and easier to expand if new bracket types are added.
        bracket_map = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the topmost element from the stack if it's not empty
                # If it is empty, assign a dummy value ('#') that won't match any bracket
                top_element = stack.pop() if stack else '#'
                
                # If the popped opening bracket doesn't match the corresponding closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty at the end, all brackets were matched correctly.
        return not stack
