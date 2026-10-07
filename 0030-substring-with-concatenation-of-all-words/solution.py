from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        # Count the required frequency of each word
        word_count = Counter(words)
        result = []
        
        # We only need to offset our starting point 'word_len' times.
        # This allows us to cover every possible word alignment in the string.
        for i in range(word_len):
            left = i
            right = i
            seen_words = Counter()
            valid_words_count = 0
            
            # Slide a window across the string, jumping by 'word_len' at a time
            while right + word_len <= len(s):
                # Extract the next word from the right side of the window
                current_word = s[right:right + word_len]
                right += word_len
                
                if current_word in word_count:
                    seen_words[current_word] += 1
                    valid_words_count += 1
                    
                    # If we have collected too many of the current word, 
                    # shrink the window from the left until it's valid again.
                    while seen_words[current_word] > word_count[current_word]:
                        left_word = s[left:left + word_len]
                        seen_words[left_word] -= 1
                        valid_words_count -= 1
                        left += word_len
                        
                    # If our window has exactly the right number of words, record the starting index
                    if valid_words_count == num_words:
                        result.append(left)
                else:
                    # If we hit a word that isn't in our list at all, the continuous chain is broken.
                    # Reset the window completely.
                    seen_words.clear()
                    valid_words_count = 0
                    left = right
                    
        return result
