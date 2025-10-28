import sys

def solve_random_walk():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1
    results = []
    
    for _ in range(T):
        A = int(input[idx]); B = int(input[idx+1]); idx += 2
        p = float(input[idx]); q = float(input[idx+1]); r = float(input[idx+2]); idx += 3
        
        # Number of positions from A to B inclusive
        n = B - A + 1
        positions = list(range(A, B + 1))
        
        # Build the system of equations for E(x)
        # E(x) = 1 + p*E(x+1) + q*E(x-1) + r*E(x)
        # Rearranged: E(x) - p*E(x+1) - q*E(x-1) - r*E(x) = 1
        # So: (1-r)*E(x) - p*E(x+1) - q*E(x-1) = 1
        
        # Coefficient matrix (n x n)
        coeff = [[0.0] * n for _ in range(n)]
        # Right-hand side vector
        rhs = [1.0] * n  # All equations have constant term 1
        
        for i, x in enumerate(positions):
            if x == A or x == B:
                # Boundary conditions: E(A) = 0, E(B) = 0
                coeff[i][i] = 1.0
                rhs[i] = 0.0  # Override the 1.0 for boundaries
            else:
                coeff[i][i] = 1.0 - r
                
                # E(x+1) term
                x_plus_1 = x + 1
                if A <= x_plus_1 <= B:
                    j_plus = positions.index(x_plus_1)
                    coeff[i][j_plus] = -p
                
                # E(x-1) term  
                x_minus_1 = x - 1
                if A <= x_minus_1 <= B:
                    j_minus = positions.index(x_minus_1)
                    coeff[i][j_minus] = -q
        
        # Solve the linear system using Gaussian elimination
        E = gaussian_elimination(coeff, rhs, n)
        
        # Find the expected steps from position 0
        zero_index = positions.index(0)
        expected_steps = E[zero_index]
        results.append(f"{expected_steps:.6f}")
    
    return results

def gaussian_elimination(coeff, rhs, n):
    """Solve system of linear equations using Gaussian elimination"""
    # Create augmented matrix
    aug = [[0.0] * (n + 1) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            aug[i][j] = coeff[i][j]
        aug[i][n] = rhs[i]
    
    # Forward elimination
    for i in range(n):
        # Partial pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(aug[k][i]) > abs(aug[max_row][i]):
                max_row = k
        aug[i], aug[max_row] = aug[max_row], aug[i]
        
        # Skip if pivot is zero (will be handled in back substitution)
        if abs(aug[i][i]) < 1e-12:
            continue
            
        # Eliminate below
        for k in range(i + 1, n):
            factor = aug[k][i] / aug[i][i]
            for j in range(i, n + 1):
                aug[k][j] -= factor * aug[i][j]
    
    # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        if abs(aug[i][i]) < 1e-12:
            if abs(aug[i][n]) > 1e-12:
                # Inconsistent system - this shouldn't happen in our problem
                x[i] = 0.0
            else:
                x[i] = 0.0  # Free variable
        else:
            x[i] = aug[i][n]
            for j in range(i + 1, n):
                x[i] -= aug[i][j] * x[j]
            x[i] /= aug[i][i]
    
    return x