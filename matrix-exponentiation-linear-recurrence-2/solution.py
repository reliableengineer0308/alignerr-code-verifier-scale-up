import sys

def mat_mult(A, B, mod):
    """Multiply two matrices A and B modulo mod"""
    n = len(A)
    m = len(B[0])
    p = len(B)
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % mod
    return result

def mat_pow(matrix, power, mod):
    """Matrix exponentiation using fast power"""
    n = len(matrix)
    
    # Initialize result as identity matrix
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = [row[:] for row in matrix]
    
    while power > 0:
        if power & 1:
            result = mat_mult(result, base, mod)
        base = mat_mult(base, base, mod)
        power //= 2
    
    return result

def solve_linear_recurrence():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1
    results = []
    
    for _ in range(T):
        k = int(input[idx]); n = int(input[idx+1]); M = int(input[idx+2]); idx += 3
        
        # Read coefficients
        coeffs = []
        for i in range(k):
            coeffs.append(int(input[idx])); idx += 1
        
        # Read initial values
        initial = []
        for i in range(k):
            initial.append(int(input[idx])); idx += 1
        
        if n < k:
            # Direct lookup from initial values
            results.append(str(initial[n] % M))
            continue
        
        # Build transformation matrix
        # The matrix is k x k
        transform = [[0] * k for _ in range(k)]
        
        # First row: recurrence coefficients
        for i in range(k):
            transform[0][i] = coeffs[i] % M
        
        # Lower rows: identity shift
        for i in range(1, k):
            transform[i][i-1] = 1 % M
        
        # Compute transform^(n - k + 1)
        power = n - k + 1
        transform_pow = mat_pow(transform, power, M)
        
        # Compute result: first row of transform_pow × initial vector
        result = 0
        for i in range(k):
            result = (result + transform_pow[0][i] * initial[k-1-i]) % M
        
        results.append(str(result))
    
    return results

if __name__ == "__main__":
    results = solve_linear_recurrence()
    for result in results:
        print(result)