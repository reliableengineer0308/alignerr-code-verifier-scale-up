from collections import Counter
import math

def count_unique_permutations(s):
    """
    Count the number of unique permutations of a string with possible duplicates.
    
    Args:
        s (str or List[str]): Input string or list of characters
    
    Returns:
        int: Number of unique permutations
    """
    if not s or len(s) == 0:
        return 1
    
    n = len(s)
    
    # Count frequency of each character
    freq = Counter(s)
    
    # Compute n!
    total = math.factorial(n)
    
    # Divide by factorial of each frequency
    for count in freq.values():
        total //= math.factorial(count)
    
    
    return total
