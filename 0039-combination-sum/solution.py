class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(remain: int, combo: list[int], start: int):
            # Base Case 1: We hit the exact target! Add a copy of the combo to results.
            if remain == 0:
                result.append(list(combo))
                return
                
            # Base Case 2: We exceeded the target. This path is dead.
            if remain < 0:
                return
                
            # Iterate through the candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                # Make a choice: Add the current number to our combination
                combo.append(candidates[i])
                
                # Recursively explore with the new remaining target.
                # CRITICAL: We pass 'i' (not i + 1) because we are allowed to reuse the same number.
                backtrack(remain - candidates[i], combo, i)
                
                # Undo the choice (Backtrack) to explore the next candidate
                combo.pop()
                
        # Start the recursion with the full target, an empty combination, and index 0
        backtrack(target, [], 0)
        return result
