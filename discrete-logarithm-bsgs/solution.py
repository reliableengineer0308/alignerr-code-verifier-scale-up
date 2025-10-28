import math

def discrete_logarithm(p, g, h):
    """
    Solve g^x ≡ h (mod p) using Baby-Step Giant-Step algorithm
    Returns smallest non-negative x, or -1 if no solution
    """
    if h == 1:
        return 0
    if g == 0:
        return 0 if h == 0 else -1
    
    # Special case: if g is 1, then solution exists only if h is 1
    if g == 1:
        return 0 if h == 1 else -1
    
    n = p - 1  # By Fermat's little theorem
    m = int(math.isqrt(n)) + 1
    
    # Baby step: precompute g^j mod p for j = 0 to m-1
    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * g) % p
    
    # Precompute g^(-m) mod p
    g_inv_m = pow(g, n - m, p)  # g^(-m) = g^(p-1-m) mod p
    
    # Giant step
    giant = h
    for i in range(m):
        if giant in baby_steps:
            j = baby_steps[giant]
            x = i * m + j
            if pow(g, x, p) == h:  # Verify solution
                return x
        giant = (giant * g_inv_m) % p
    
    return -1

def solve_discrete_log():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        p = int(input[idx])
        g = int(input[idx + 1])
        h = int(input[idx + 2])
        idx += 3
        
        result = discrete_logarithm(p, g, h)
        results.append(str(result))
    
    return results