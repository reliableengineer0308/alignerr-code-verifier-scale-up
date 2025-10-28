def is_match(s: str, p: str) -> bool:
    """
    Checks if string s matches pattern p with wildcards '?' and '*'.
    
    '?' matches any single character.
    '*' matches any sequence of characters (including empty).
    
    Uses dynamic programming for O(mn) time complexity.
    
    Args:
        s (str): Input string to match
        p (str): Pattern string with '?' and '*' wildcards
    
    Returns:
        bool: True if s fully matches p, False otherwise
    
    Examples:
        >>> is_match("aa", "a")
        False
        >>> is_match("aa", "*")
        True
        >>> is_match("cb", "?a")
        False
        >>> is_match("adceb", "*a*b")
        True
        >>> is_match("acdcb", "a*c?b")
        False
    """
    m, n = len(s), len(p)
    
    # DP table: dp[i][j] = whether s[:i] matches p[:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns like "***" that match empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' matches empty (dp[i][j-1]) or extends match (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # '?' matches any char, or exact char match
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = False  # No match
    
    return dp[m][n]




# Alternative recursive solution with memoization (for reference)
def is_match_recursive(s: str, p: str) -> bool:
    """Recursive implementation with memoization."""
    memo = {}
    
    def match(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        
        
        # Base cases
        if j == len(p):
            return i == len(s)
        
        # Pattern has '*' at current position
        if p[j] == '*':
            # Match empty or consume one char from s
            result = match(i, j + 1) or (i < len(s) and match(i + 1, j))
        else:
            # Exact match or '?'
            first_match = i < len(s) and (p[j] == '?' or s[i] == p[j])
            result = first_match and match(i + 1, j + 1)
        
        
        memo[(i, j)] = result
        return result
    
    
    return match(0, 0)
