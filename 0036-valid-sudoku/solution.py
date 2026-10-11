class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create an array of 9 empty sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                    
                # Calculate which of the 9 sub-boxes we are currently inside
                box_idx = (r // 3) * 3 + (c // 3)
                
                # If we've already seen this value in the current row, col, or box, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                    
                # Otherwise, record that we've seen this value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        # If we check every filled cell and find no duplicates, the board is valid
        return True
