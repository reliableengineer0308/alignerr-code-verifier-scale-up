MOD = 10**9 + 7

def mat_mult(A, B):
    """Multiply two matrices A and B modulo MOD"""
    k = len(A)
    C = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            for l in range(k):
                C[i][j] = (C[i][j] + A[i][l] * B[l][j]) % MOD
    return C

def mat_pow(matrix, power):
    """Fast matrix exponentiation"""
    k = len(matrix)
    # Initialize result as identity matrix
    result = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
    base = matrix
    
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        power //= 2
    
    return result

def solve_linear_recurrence(k, coefficients, initial, n):
    if n <= k:
        return initial[n-1] % MOD
    
    # Build transformation matrix
    matrix = [[0] * k for _ in range(k)]
    for i in range(k):
        matrix[0][i] = coefficients[i] % MOD
    for i in range(1, k):
        matrix[i][i-1] = 1
    
    # Compute matrix^(n-k)
    power = n - k
    M_pow = mat_pow(matrix, power)
    
    # Multiply with initial vector
    result = 0
    for i in range(k):
        result = (result + M_pow[0][i] * initial[k-1-i]) % MOD
    
    return result

def process_input(input_data):
    lines = input_data.strip().split('\n')
    k = int(lines[0])
    coefficients = list(map(int, lines[1].split()))
    initial = list(map(int, lines[2].split()))
    n = int(lines[3])
    
    return solve_linear_recurrence(k, coefficients, initial, n)