def is_balanced(s):
    """
    Checks if parentheses in string are balanced.
    
    Args:
        s (str): Input string with brackets and other characters
        
    Returns:
        bool: True if balanced, False otherwise
    """
    stack = []
    # Mapping of closing to opening brackets
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in '([{':
            # Push opening brackets onto stack
            stack.append(char)
        elif char in ')]}':
            # Closing bracket: check if matches last opened
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # If stack is empty, all brackets were matched
    return len(stack) == 0
