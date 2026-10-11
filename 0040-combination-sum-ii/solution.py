class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Sort the array first to handle duplicates and enable early stopping
        candidates.sort()
        result = []
        
        def backtrack(remain: int, combo: list[int], start: int):
            # Base Case 1: We hit the exact target
            if remain == 0:
                result.append(list(combo))
                return
                
            for i in range(start, len(candidates)):
                # Skip duplicate elements at the exact same depth of the recursion tree
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                # Optimization: Since the array is sorted, if the current number 
                # exceeds the remaining target, all subsequent numbers will too.
                if candidates[i] > remain:
                    break
                    
                # Make a choice
                combo.append(candidates[i])
                
                # Recursively explore. 
                # CRITICAL: We pass 'i + 1' because we can only use each number once.
                backtrack(remain - candidates[i], combo, i + 1)
                
                # Undo the choice (Backtrack)
                combo.pop()
                
        # Start recursion with the full target, an empty combination, and index 0
        backtrack(target, [], 0)
        return result
