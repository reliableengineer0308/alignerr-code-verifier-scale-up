import heapq

def solve(data):
    idx = 0
    N = data[idx]; idx += 1
    M = data[idx]; idx += 1
    S = data[idx]; idx += 1
    D = data[idx]; idx += 1
    
    # Read processing times
    proc = data[idx:idx+N]
    idx += N
    
    # Build graph
    graph = [[] for _ in range(N)]
    for i in range(M):
        u, v, t = data[idx], data[idx+1], data[idx+2]
        idx += 3
        graph[u].append((v, t))
        graph[v].append((u, t))
    
    # Modified Dijkstra: dist[u] represents time when we FINISH processing at u
    dist = [float('inf')] * N
    dist[S] = proc[S]  # Time to finish processing at source
    
    pq = [(proc[S], S)]
    
    while pq:
        current_time, u = heapq.heappop(pq)
        
        if current_time > dist[u]:
            continue
            
        if u == D:
            # If we reach destination, we're done (no processing at destination)
            continue
            
        for v, trans in graph[u]:
            # Time to reach v from u: current_time + transmission
            arrival_at_v = current_time + trans
            
            # If v is destination, we're done
            if v == D:
                if arrival_at_v < dist[v]:
                    dist[v] = arrival_at_v
                    heapq.heappush(pq, (arrival_at_v, v))
            else:
                # For intermediate nodes, add processing time
                finish_processing_at_v = arrival_at_v + proc[v]
                if finish_processing_at_v < dist[v]:
                    dist[v] = finish_processing_at_v
                    heapq.heappush(pq, (finish_processing_at_v, v))
    
    return dist[D] if dist[D] != float('inf') else -1