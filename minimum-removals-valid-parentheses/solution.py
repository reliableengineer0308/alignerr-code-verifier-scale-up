def min_removals_to_valid(s: str) -> int:
    """
    Returns the minimum number of parentheses removals to make s a valid parentheses string.
    
    Time: O(n), Space: O(1)
    """
    if not s:
        return 0

    balance = 0
    removals = 0

    # Left-to-right pass: catch excess ')'
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:  # More ')' than '('
                removals += 1
                balance = 0  # Reset balance after removal

    # After pass: any remaining '(' are unmatched
    removals += balance  # These are excess '('

    return removals
