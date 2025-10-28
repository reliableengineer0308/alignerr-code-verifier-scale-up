from collections import deque

def solve_maze(grid):
    # Find start and target positions
    start = target = None
    n, m = len(grid), len(grid[0])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'T':
                target = (i, j)
    
    # BFS initialization
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    visited = [[False] * m for _ in range(n)]
    parent = {}  # stores (prev_r, prev_c, move_direction)
    
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True
    parent[start] = (None, None, None)  # start has no parent
    
    found = False
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == target:
            found = True
            break
            
        for dr, dc, move in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < n and 0 <= nc < m and 
                not visited[nr][nc] and 
                grid[nr][nc] != '#'):
                visited[nr][nc] = True
                parent[(nr, nc)] = (r, c, move)
                queue.append((nr, nc, dist + 1))
    
    if not found:
        return -1, [] # No path.
    
    # Reconstruct path
    path_moves = []
    current = target
    while current != start:
        r, c = current
        prev_r, prev_c, move = parent[current]
        path_moves.append(move)
        current = (prev_r, prev_c)
    
    path_moves.reverse()
    return len(path_moves), path_moves