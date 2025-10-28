import math

def extended_gcd(a, b):
    """Extended Euclidean Algorithm - returns (gcd, x, y) such that a*x + b*y = gcd"""
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)

def solve_diophantine(a, b, c):
    """Solve a*x + b*y = c, return solution with smallest non-negative x"""
    # Special case: both coefficients are zero
    if a == 0 and b == 0:
        return "No Solution" if c != 0 else "0 0"
    
    # Special case: one coefficient is zero
    if a == 0:
        if c % b == 0:
            y = c // b
            return f"0 {y}"
        else:
            return "No Solution"
    
    if b == 0:
        if c % a == 0:
            x = c // a
            return f"{x} 0"
        else:
            return "No Solution"
    
    # Handle negative coefficients by working with absolute values
    abs_a, abs_b = abs(a), abs(b)
    g, x0, y0 = extended_gcd(abs_a, abs_b)
    
    # Check if solution exists
    if c % g != 0:
        return "No Solution"
    
    # Scale the particular solution
    multiplier = c // g
    x0 *= multiplier
    y0 *= multiplier
    
    # Adjust signs based on original coefficients
    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0
    
    # General solution:
    # x = x0 + (b/g) * t
    # y = y0 - (a/g) * t
    # where t is any integer
    
    bg = b // g
    ag = a // g
    
    # We want the smallest non-negative x
    if bg == 0:
        # This means b = 0, but we already handled that case
        return f"{x0} {y0}" if x0 >= 0 else "No Solution"
    
    # Find t such that x0 + (b/g)*t >= 0
    if bg > 0:
        # We need: x0 + (b/g)*t >= 0
        # => t >= -x0 * g / b
        t_min = math.ceil(-x0 * g / b)
    else:
        # bg < 0
        # We need: x0 + (b/g)*t >= 0  
        # => t <= -x0 * g / b  (since dividing by negative flips inequality)
        t_min = math.floor(-x0 * g / b)
    
    # Calculate the solution for t_min
    x = x0 + bg * t_min
    y = y0 - ag * t_min
    
    # Verify this is indeed a solution with non-negative x
    if a * x + b * y == c and x >= 0:
        return f"{x} {y}"
    else:
        # Try t_min + 1 and t_min - 1 to handle rounding issues
        for delta in [-1, 0, 1, 2]:
            t_test = t_min + delta
            x_test = x0 + bg * t_test
            y_test = y0 - ag * t_test
            if a * x_test + b * y_test == c and x_test >= 0:
                return f"{x_test} {y_test}"
        return "No Solution"

def solve_diophantine_equations():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        a = int(input[idx])
        b = int(input[idx + 1])
        c = int(input[idx + 2])
        idx += 3
        
        result = solve_diophantine(a, b, c)
        results.append(result)
    
    return results