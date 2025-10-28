def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def modular_inverse_crt(a, m):
    """Find modular inverse of a modulo m for CRT"""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    return x % m

def chinese_remainder_theorem(congruences):
    """
    Solve system of congruences: x ≡ a_i (mod m_i)
    Returns smallest non-negative solution, or -1 if no solution
    """
    k = len(congruences)
    
    # Check pairwise coprimality and find overall product
    M = 1
    for i in range(k):
        M *= congruences[i][1]
    
    # Verify consistency for non-coprime moduli
    for i in range(k):
        for j in range(i + 1, k):
            a1, m1 = congruences[i]
            a2, m2 = congruences[j]
            gcd = extended_gcd(m1, m2)[0]
            if (a1 % gcd) != (a2 % gcd):
                return -1
    
    # Solve using CRT
    solution = 0
    for i in range(k):
        a_i, m_i = congruences[i]
        M_i = M // m_i
        y_i = modular_inverse_crt(M_i, m_i)
        if y_i is None:
            return -1
        solution = (solution + a_i * M_i * y_i) % M
    
    return solution

def solve_chinese_remainder():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        k = int(input[idx])
        idx += 1
        
        congruences = []
        for _ in range(k):
            a = int(input[idx])
            m = int(input[idx + 1])
            idx += 2
            congruences.append((a, m))
        
        result = chinese_remainder_theorem(congruences)
        results.append(str(result))
    
    return results
