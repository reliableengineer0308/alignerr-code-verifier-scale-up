def rotate_matrix(matrix):
    """
    Rotates an n×n matrix 90 degrees clockwise in-place.
    
    Uses the transpose-then-reverse method:
    1. Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    2. Reverse each row of the transposed matrix.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    Args:
        matrix (List[List[int]]): n×n square matrix to rotate
    """
    n = len(matrix)
    if n <= 1:
        return  # Nothing to rotate

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1



# Alternative implementation: Cyclic rotation (layer-by-layer)
def rotate_matrix_cyclic(matrix):
    """
    Alternative implementation using cyclic rotation of layers.
    Rotates each concentric layer by swapping groups of 4 elements.
    """
    n = len(matrix)
    if n <= 1:
        return

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top element
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Assign top to right
            matrix[i][last] = top
