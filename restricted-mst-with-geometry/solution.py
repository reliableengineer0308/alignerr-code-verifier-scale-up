from heapq import heappush, heappop

from collections import defaultdict

def min_cost_connect_points(points: list[list[int]], forbidden_edges: list[tuple[int, int]]) -> int:
    n = len(points)
    if n == 1:
        return 0

    # Build adjacency list with allowed edges
    adj = defaultdict(list)
    forbidden_set = set((u, v) if u < v else (v, u) for u, v in forbidden_edges)

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in forbidden_set:
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

    # Check connectivity using BFS/DFS from node 0
    visited = [False] * n
    stack = [0]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        for _, neighbor in adj[node]:
            if not visited[neighbor]:
                stack.append(neighbor)

    if not all(visited):
        return -1  # Graph is disconnected due to forbidden edges

    # Prim's algorithm for MST on allowed edges
    heap = [(0, 0)]  # (cost, node)
    mst_cost = 0
    in_mst = [False] * n

    while heap:
        cost, u = heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        mst_cost += cost
        for edge_cost, v in adj[u]:
            if not in_mst[v]:
                heappush(heap, (edge_cost, v))

    return mst_cost
