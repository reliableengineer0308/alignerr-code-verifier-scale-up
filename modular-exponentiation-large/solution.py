def modular_exponentiation(a, b, m):
    """
    Compute a^b mod m using fast exponentiation
    """
    if m == 1:
        return 0
    
    if b == 0:
        return 1
    
    result = 1
    a = a % m
    
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        
        a = (a * a) % m
        b //= 2
    
    return result

def solve_modular_exponentiation():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        a = int(input[idx])
        b = int(input[idx + 1])
        m = int(input[idx + 2])
        idx += 3
        
        result = modular_exponentiation(a, b, m)
        results.append(str(result))
    
    return results