def modular_inverse(a, m):
    """
    Compute modular inverse of a under modulo m using Fermat's Little Theorem.
    Returns -1 if inverse doesn't exist.
    """
    # If a is divisible by m, no inverse exists
    if a % m == 0:
        return -1
    
    # Compute a^(m-2) mod m using fast exponentiation
    return pow(a, m-2, m)

def solve_modular_inverse():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        a = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        result = modular_inverse(a, m)
        results.append(str(result))
    
    return results