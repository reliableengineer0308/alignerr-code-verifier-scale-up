import sys
import heapq

def dijkstra(n, edges, S, T):
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # Initialize arrays
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[S] = 0
    
    # Priority queue: (distance, node)
    pq = [(0, S)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Skip if we found a better path already
        if current_dist > dist[u]:
            continue
            
        if u == T:
            break
            
        for v, w in graph[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))
    
    if dist[T] == float('inf'):
        return -1, []
    
    # Reconstruct path
    path = []
    current = T
    while current != -1:
        path.append(current)
        current = prev[current]
    path.reverse()
    
    return dist[T], path

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); m = int(data[idx+1]); idx += 2
    S = int(data[idx]); T = int(data[idx+1]); idx += 2
    
    edges = []
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2]); idx += 3
        edges.append((u, v, w))
    
    distance, path = dijkstra(n, edges, S, T)
    
    if distance == -1:
        print("No path")
        return []
    else:
        print(f"Shortest distance: {distance}")
        path_str = " → ".join(map(str, path))
        print(f"Shortest path: {path_str}")
        return path

if __name__ == "__main__":
    main()