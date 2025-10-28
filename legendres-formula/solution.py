def legendre_exponent(n, p):
    """
    Compute the exponent of prime p in n! using Legendre's formula
    """
    if n == 0 or n == 1:
        return 0
    
    exponent = 0
    power = p
    
    while power <= n:
        exponent += n // power
        # Check for integer overflow
        if power > n // p:  # Prevent overflow
            break
        power *= p
    
    return exponent

def solve_legendre_formula():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        p = int(input[idx + 1])
        idx += 2
        
        result = legendre_exponent(n, p)
        results.append(str(result))
    
    return results