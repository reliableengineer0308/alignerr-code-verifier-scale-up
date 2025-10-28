def matrix_permanent(matrix, n, mod):
    """
    Compute permanent of n×n matrix modulo mod using DP with bitmask
    """
    # dp[mask] = sum of products for assigning first k rows to columns in mask
    # where k = popcount(mask)
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for mask in range(1 << n):
        i = bin(mask).count('1')  # number of rows assigned so far
        if i >= n:
            continue
            
        for j in range(n):
            if not (mask >> j) & 1:  # if column j is not used
                new_mask = mask | (1 << j)
                dp[new_mask] = (dp[new_mask] + dp[mask] * matrix[i][j]) % mod
    
    return dp[(1 << n) - 1]

def solve_matrix_permanent():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        matrix = []
        for i in range(n):
            row = list(map(int, input[idx:idx + n]))
            idx += n
            matrix.append(row)
        
        result = matrix_permanent(matrix, n, m)
        results.append(str(result))
    
    return results