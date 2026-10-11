class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"
            
        # Start with the very first sequence
        current_string = "1"
        
        # Iteratively build the sequence up to n
        for _ in range(2, n + 1):
            next_string = []
            count = 1
            
            # Scan the current string to generate the next one
            for i in range(1, len(current_string)):
                # If the current character matches the previous one, increment the count
                if current_string[i] == current_string[i - 1]:
                    count += 1
                else:
                    # Character changed. Record the count and the previous character.
                    next_string.append(str(count))
                    next_string.append(current_string[i - 1])
                    # Reset the count for the new character
                    count = 1
                    
            # After the loop ends, we must append the final counted group
            next_string.append(str(count))
            next_string.append(current_string[-1])
            
            # Join the list into a string for the next iteration
            current_string = "".join(next_string)
            
        return current_string
