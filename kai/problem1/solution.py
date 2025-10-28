import heapq
import sys

def solve(data):    
    # Parse first line
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    # Build adjacency list
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        w = int(data[idx]); idx += 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Dijkstra's algorithm
    dist = [float('inf')] * N
    dist[S] = 0
    heap = [(0, S)]  # (distance, node)
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        # Early termination if we reached target
        if u == T:
            return current_dist
            
        # Skip if we found a better distance already
        if current_dist > dist[u]:
            continue
            
        # Explore neighbors
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    
    return -1 if dist[T] == float('inf') else dist[T]
