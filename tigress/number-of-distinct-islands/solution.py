from typing import List, Tuple, Set

def numDistinctIslands(grid: List[List[int]]) -> int:
    """
    Counts distinct island shapes in a binary grid using DFS.
    Two islands are identical if their relative coordinate patterns match after translation.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    distinct_shapes: Set[Tuple[Tuple[int, int], ...]] = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right


    def dfs(r: int, c: int, base_r: int, base_c: int) -> List[Tuple[int, int]]:
        """Returns list of (dr, dc) relative to base cell."""
        # Base case: out of bounds, water, or already visited
        if (r < 0 or r >= m or c < 0 or c >= n or 
                visited[r][c] or grid[r][c] == 0):
            return []  # Return empty list, NOT None


        visited[r][c] = True
        rel_r, rel_c = r - base_r, c - base_c
        points = [(rel_r, rel_c)]


        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            points.extend(dfs(nr, nc, base_r, base_c))


        return points

    # Scan every cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                island_points = dfs(i, j, i, j)
                # Normalize: sort to make order-independent, convert to tuple for hashing
                shape_key = tuple(sorted(island_points))
                distinct_shapes.add(shape_key)


    return len(distinct_shapes)
