class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base case: if the string has reached the maximum length (n pairs = 2n characters)
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
                
            # Rule 1: We can always add an opening parenthesis if we haven't reached 'n'
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: We can only add a closing parenthesis if we have unmatched opening ones
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
