import sys

def gaussian_elimination(augmented_matrix, n):
    """
    Solve linear system using Gaussian elimination with partial pivoting
    Returns: (status, solution)
    status: 'unique', 'no_solution', 'infinite'
    """
    matrix = [row[:] for row in augmented_matrix]
    
    # Forward elimination with partial pivoting
    for col in range(n):
        # Partial pivoting: find row with maximum element in current column
        max_row = col
        for row in range(col + 1, n):
            if abs(matrix[row][col]) > abs(matrix[max_row][col]):
                max_row = row
        
        # Swap rows
        matrix[col], matrix[max_row] = matrix[max_row], matrix[col]
        
        # If pivot is zero, check if system is inconsistent or has infinite solutions
        if abs(matrix[col][col]) < 1e-12:
            # Check if this makes the system inconsistent
            for row in range(col, n):
                if abs(matrix[row][n]) > 1e-12:  # Non-zero constant term
                    # Check if all coefficients in this row are zero
                    all_zero = True
                    for c in range(col, n):
                        if abs(matrix[row][c]) > 1e-12:
                            all_zero = False
                            break
                    if all_zero:
                        return 'no_solution', None
            return 'infinite', None
        
        # Eliminate below
        for row in range(col + 1, n):
            factor = matrix[row][col] / matrix[col][col]
            for c in range(col, n + 1):
                matrix[row][c] -= factor * matrix[col][c]
    
    # Back substitution
    x = [0.0] * n
    for row in range(n - 1, -1, -1):
        # Check for inconsistency
        if abs(matrix[row][row]) < 1e-12:
            if abs(matrix[row][n]) > 1e-12:
                return 'no_solution', None
            else:
                return 'infinite', None
        
        x[row] = matrix[row][n]
        for col in range(row + 1, n):
            x[row] -= matrix[row][col] * x[col]
        x[row] /= matrix[row][row]
    
    return 'unique', x

def solve_linear_system():
    input = sys.stdin.read().split()
    if not input:
        return []
    
    idx = 0
    n = int(input[idx]); idx += 1
    
    # Read augmented matrix
    matrix = []
    for i in range(n):
        row = []
        for j in range(n + 1):
            row.append(float(input[idx])); idx += 1
        matrix.append(row)
    
    status, solution = gaussian_elimination(matrix, n)
    
    if status == 'unique':
        result = ["Solution"]
        for val in solution:
            result.append(f"{val:.6f}")
        return result
    elif status == 'no_solution':
        return ["No solution"]
    else:  # infinite
        return ["Infinite solutions"]

if __name__ == "__main__":
    results = solve_linear_system()
    for result in results:
        print(result)