from typing import List

def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    Finds the minimum cost to connect all points using Prim's algorithm.
    
    Time: O(n²), Space: O(n)
    Uses Manhattan distance as edge weight.
    
    Args:
        points: List of [x, y] coordinates
        
    Returns:
        Minimum total cost to connect all points (MST weight)
    """
    n = len(points)
    if n <= 1:
        return 0

    # Minimum distance from each node to the current MST
    min_dist = [float('inf')] * n
    min_dist[0] = 0  # Start from node 0
    visited = [False] * n
    total_cost = 0

    for _ in range(n):
        # Find the node with minimum distance to MST
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i

        if u == -1:
            break  # No unvisited node found (should not happen)

        visited[u] = True
        total_cost += min_dist[u]

        # Update distances for all unvisited nodes
        for v in range(n):
            if not visited[v]:
                # Manhattan distance
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dist < min_dist[v]:
                    min_dist[v] = dist

    return total_cost
