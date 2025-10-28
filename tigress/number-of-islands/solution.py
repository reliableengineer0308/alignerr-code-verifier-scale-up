def num_islands(grid):
    """
    Counts the number of islands using DFS.
    Time: O(m * n), Space: O(m * n) [recursion stack in worst case]
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # Check bounds and if it's land
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        # Mark as visited by turning '1' into '0'
        grid[r][c] = '0'
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)  # This will mark the entire island as visited
                count += 1

    return count
