class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Bitmasks to keep track of used numbers in O(1) time
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        # Step 1: Record the initial state of the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c])
                    bit = 1 << val
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + (c // 3)] |= bit
                    
        def backtrack(r: int, c: int) -> bool:
            # If we reach the end of a row, wrap around to the next row
            if c == 9:
                c = 0
                r += 1
                # If we move past the last row, the board is perfectly solved
                if r == 9:
                    return True 
                    
            # If the cell is already filled, skip to the next one
            if board[r][c] != '.':
                return backtrack(r, c + 1)
                
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Step 2: Try guessing digits 1 through 9
            for val in range(1, 10):
                bit = 1 << val
                
                # O(1) check: Is this bit already set in the row, col, or box?
                if not (rows[r] & bit) and not (cols[c] & bit) and not (boxes[box_idx] & bit):
                    
                    # Make the choice
                    board[r][c] = str(val)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box_idx] |= bit
                    
                    # Recursively try to solve the rest
                    if backtrack(r, c + 1):
                        return True
                        
                    # Undo the choice (Backtrack)
                    board[r][c] = '.'
                    rows[r] &= ~bit
                    cols[c] &= ~bit
                    boxes[box_idx] &= ~bit
                    
            return False

        backtrack(0, 0)
