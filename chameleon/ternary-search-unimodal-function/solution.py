def quadratic_function(x, a, b, c):
    """
    Evaluate quadratic function f(x) = -a*x² + b*x + c
    The negative sign ensures it's a downward-opening parabola (unimodal)
    """
    return -a * x * x + b * x + c

def ternary_search_max(left, right, a, b, c, precision=1e-7):
    """
    Find the x that maximizes f(x) = -a*x² + b*x + c in range [left, right]
    using ternary search
    """
    while right - left > precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        
        f1 = quadratic_function(mid1, a, b, c)
        f2 = quadratic_function(mid2, a, b, c)
        
        if f1 < f2:
            left = mid1
        else:
            right = mid2
    
    return (left + right) / 2

def solve_ternary_search():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        left = float(input[idx])
        right = float(input[idx + 1])
        idx += 2
        
        a = float(input[idx])
        b = float(input[idx + 1])
        c = float(input[idx + 2])
        idx += 3
        
        # For quadratic function, the vertex is at x = b/(2a)
        # But we need to check if it's within bounds
        vertex = b / (2 * a)
        
        if vertex < left:
            result = left
        elif vertex > right:
            result = right
        else:
            result = vertex
        
        # Use ternary search to verify (though we know the analytical solution)
        ternary_result = ternary_search_max(left, right, a, b, c)
        
        # For quadratic functions, both methods should give same result
        # We'll use the analytical solution for better accuracy
        results.append(f"Case #{case_num}: {result:.6f}")
    
    return results