from collections import defaultdict, Counter
from typing import List

class SlidingWindowMode:
    def find_mode_in_window(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the mode of each sliding window of size k.
        In case of tie in frequency, returns the smallest element.
        
        Time: O(n), Space: O(k)
        """
        if k == 1:
            return nums
        
        n = len(nums)
        result = []
        
        # Frequency map for current window
        freq = defaultdict(int)
        # Count of elements per frequency
        freq_count = defaultdict(set)
        max_freq = 0
        
        def add_element(x):
            nonlocal max_freq
            old_freq = freq[x]
            freq[x] += 1
            new_freq = old_freq + 1
            
            # Remove from old frequency group
            if old_freq > 0:
                freq_count[old_freq].discard(x)
            # Add to new frequency group
            freq_count[new_freq].add(x)
            
            if new_freq > max_freq:
                max_freq = new_freq
        
        def remove_element(x):
            nonlocal max_freq
            old_freq = freq[x]
            freq[x] -= 1
            new_freq = old_freq - 1
            
            freq_count[old_freq].discard(x)
            if new_freq > 0:
                freq_count[new_freq].add(x)
            else:
                del freq[x]  # Remove if freq becomes 0
            
            # Update max_freq if needed
            while max_freq > 0 and not freq_count[max_freq]:
                max_freq -= 1
        
        
        # Initialize first window
        for i in range(k):
            add_element(nums[i])
        
        # Get mode for first window
        mode = min(freq_count[max_freq])
        result.append(mode)
        
        # Slide window
        for i in range(k, n):
            # Remove leftmost element of previous window
            remove_element(nums[i - k])
            # Add new rightmost element
            add_element(nums[i])
            # Get current mode
            mode = min(freq_count[max_freq])
            result.append(mode)
            
        return result


# Wrapper function for direct use
def sliding_window_mode(nums: List[int], k: int) -> List[int]:
    solver = SlidingWindowMode()
    return solver.find_mode_in_window(nums, k)
