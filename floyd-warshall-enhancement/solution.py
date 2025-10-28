def floyd_warshall_enhanced(graph):
    n = len(graph)
    
    # Инициализация расстояний с обязательной нормализацией диагонали
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = graph[i][j]
        distances[i][i] = 0  # Нормализация диагонали


    parents = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] != float('inf'):
                parents[i][j] = i

    # Основной цикл Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (distances[i][k] != float('inf') and 
                    distances[k][j] != float('inf') and
                    distances[i][j] > distances[i][k] + distances[k][j]):
                    distances[i][j] = distances[i][k] + distances[k][j]
                    parents[i][j] = parents[k][j]


    # Проверка на отрицательные циклы: можно ли улучшить путь i → i?
    has_negative_cycle = False
    for i in range(n):
        for k in range(n):
            # Если есть путь i → k → i короче, чем 0 (текущее distances[i][i])
            if (distances[i][k] != float('inf') and
                distances[k][i] != float('inf') and
                distances[i][k] + distances[k][i] < 0):
                has_negative_cycle = True
                break
        if has_negative_cycle:
            break

    return distances, parents, has_negative_cycle


def get_path(parents, start, end):
    """
    Reconstruct path from start to end using parent matrix.
    
    Args:
        parents: 2D predecessor matrix from floyd_warshall_enhanced
        start: source vertex
        end: destination vertex
    
    Returns:
        list: Path as sequence of vertices, or empty list if no path
    """
    if parents[start][end] is None:
        return []  # No path exists
    
    
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[start][current]
    path.append(start)
    return path[::-1]  # Reverse to get start->end order