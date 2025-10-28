from typing import List, Tuple
from collections import deque

def shortest_path_dynamic(
    grid: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int],
    obstacles: List[Tuple[int, int, int]]
) -> int:
    """
    Find shortest time to reach end in a dynamic grid with time-varying obstacles.
    
    Returns minimum time or -1 if impossible.
    """
    m, n = len(grid), len(grid[0])
    start_r, start_c = start
    end_r, end_c = end

    # Precompute obstructed cells at each time
    max_t = 100
    obstructed = [set() for _ in range(max_t + 1)]
    for t, r, c in obstacles:
        if t <= max_t:
            obstructed[t].add((r, c))

    # BFS: (row, col, time)
    queue = deque()
    visited = set()

    queue.append((start_r, start_c, 0))
    visited.add((start_r, start_c, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c, t = queue.popleft()

        # Check if reached end
        if (r, c) == (end_r, end_c):
            return t

        # If time exceeds max_obstacle_time, no new obstacles appear
        if t > max_t:
            # Can move freely now
            steps = abs(r - end_r) + abs(c - end_c)
            return t + steps

        # Try all 4 directions + wait
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            nt = t + 1

            # Check bounds
            if not (0 <= nr < m and 0 <= nc < n):
                continue

            # Check permanent block
            if grid[nr][nc] == 1:
                continue

            # Check time-varying obstacle
            if (nr, nc) in obstructed[nt]:
                continue

            # Check visited
            state = (nr, nc, nt)
            if state not in visited:
                visited.add(state)
                queue.append(state)

        # Also try waiting in place
        nt = t + 1
        state = (r, c, nt)
        if state not in visited and nt <= max_t + m + n:  # Bound the wait
            visited.add(state)
            queue.append(state)

    return -1  # No path found
