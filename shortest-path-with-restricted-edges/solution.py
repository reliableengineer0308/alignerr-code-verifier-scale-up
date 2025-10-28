import heapq
from collections import defaultdict

def shortestPathWithRestrictedEdges(n, edges, restricted, start, end):
    """
    Finds shortest path from start to end avoiding restricted edges.
    Time: O((V + E) log V), Space: O(V + E)
    """
    # Convert restricted edges to set of frozensets for O(1) lookup
    restricted_set = set()
    for u, v in restricted:
        restricted_set.add(frozenset((u, v)))

    # Build adjacency list (only non-restricted edges)
    graph = defaultdict(list)
    for u, v, w in edges:
        if frozenset((u, v)) not in restricted_set:
            graph[u].append((v, w))
            graph[v].append((u, w))  # undirected


    # Dijkstra's algorithm
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)


    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == end:
            break
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))


    return dist[end] if dist[end] != float('inf') else -1

n = 100
edges = []
for i in range(0, 99, 2):  # Connect even nodes
    edges.append([i, i+1, 1])
restricted = []
print(shortestPathWithRestrictedEdges(n, edges, restricted, 0, 99))
