           
           
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
            
        # Sort the array of strings lexicographically
        strs.sort()
        
        # The longest common prefix of the entire array will always be the 
        # common prefix of the first and last strings in the sorted array.
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # Compare characters of the first and last string
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]
