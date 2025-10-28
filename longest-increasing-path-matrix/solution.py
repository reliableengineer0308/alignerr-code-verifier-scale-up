from typing import List

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    """
    Finds the length of the longest strictly increasing path in a matrix.
    
    Uses DFS with memoization (top-down dynamic programming).
    From each cell, you can move to adjacent (up/down/left/right) cells 
    only if the next cell's value is strictly greater than current.

    Time Complexity: O(m * n) — each cell visited once due to memoization
    Space Complexity: O(m * n) — for memo table and recursion stack


    Args:
        matrix: 2D list of integers (m x n)

    Returns:
        Length of the longest strictly increasing path
    """
    # Handle empty matrix
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    
    # Memoization table: stores longest path starting at (i, j)
    memo = [[-1] * n for _ in range(m)]
    
    max_path = 0  # Track global maximum path length

    # Directions for adjacent cells: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(i: int, j: int) -> int:
        """
        Returns the longest increasing path starting from cell (i, j)
        
        Uses memoization to avoid recomputation.
        """
        # If already computed, return memoized result
        if memo[i][j] != -1:
            return memo[i][j]

        best = 1  # At minimum, path includes this cell

        # Explore all 4 adjacent cells
        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Check bounds and strictly increasing condition
            if (0 <= ni < m and 0 <= nj < n
                    and matrix[ni][nj] > matrix[i][j]):
                # Recursively get path length from neighbor
                path_length = 1 + dfs(ni, nj)
                best = max(best, path_length)

        # Memoize result before returning
        memo[i][j] = best
        return best

    # Try starting DFS from every cell in the matrix
    for i in range(m):
        for j in range(n):
            max_path = max(max_path, dfs(i, j))

    return max_path
