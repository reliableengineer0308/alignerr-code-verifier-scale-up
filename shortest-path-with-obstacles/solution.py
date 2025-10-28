from collections import deque

def shortest_path_with_obstacles(grid):
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    visited = set()
    queue = deque([(0, 0, False, 0)])  # (r, c, has_ability, steps)
    visited.add((0, 0, False))
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    target = (m - 1, n - 1)
    
    if (0, 0) == target:
        return 0

    while queue:
        r, c, has_ability, steps = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                next_val = grid[nr][nc]
                next_ability = False  # Способность сбрасывается после любого хода
                
                
                if next_val == 0:
                    # Свободный ход — способность не передаётся
                    next_state = (nr, nc, False)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((nr, nc, False, steps + 1))
                        
                elif next_val == 2:
                    # Находим '2' — следующий ход можно использовать способность
                    next_state = (nr, nc, True)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((nr, nc, True, steps + 1))
                        
                elif next_val == 1:
                    # Препятствие — можно пройти только если есть способность
                    if has_ability:
                        next_state = (nr, nc, False)  # Способность потребляется
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append((nr, nc, False, steps + 1))
                
                
                # Проверка на достижение цели
                if (nr, nc) == target:
                    return steps + 1

    return -1
