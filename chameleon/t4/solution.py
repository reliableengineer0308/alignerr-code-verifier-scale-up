import sys

def solve_tsp(dist):
    n = len(dist)
    INF = 10**9
    full_mask = (1 << n) - 1
    
    # DP table: dp[mask][last] = min cost
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    # Initialize: starting from city 0
    dp[1][0] = 0
    
    # Fill DP table
    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == INF:
                continue
                
            # Try to go to next unvisited city
            for next_city in range(n):
                if mask & (1 << next_city):
                    continue  # Already visited
                if dist[last][next_city] == 0 and last != next_city:
                    continue  # No path
                    
                new_mask = mask | (1 << next_city)
                new_cost = dp[mask][last] + dist[last][next_city]
                
                if new_cost < dp[new_mask][next_city]:
                    dp[new_mask][next_city] = new_cost
                    parent[new_mask][next_city] = last
    
    # Find minimum cost to return to start
    min_cost = INF
    last_city = -1
    
    for last in range(n):
        if dp[full_mask][last] != INF and dist[last][0] != 0:
            total_cost = dp[full_mask][last] + dist[last][0]
            if total_cost < min_cost:
                min_cost = total_cost
                last_city = last
    
    if min_cost == INF:
        return "No path exists", []
    
    # Reconstruct path
    path = []
    mask = full_mask
    current = last_city
    
    while current != -1:
        path.append(current)
        prev_mask = mask ^ (1 << current)
        if prev_mask == 0:  # Reached start
            break
        current, mask = parent[mask][current], prev_mask
    
    path.reverse()
    path.append(0)  # Return to start
    
    return min_cost, path

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    dist = []
    idx = 1
    
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        idx += n
        dist.append(row)
    
    result, path = solve_tsp(dist)
    
    if result == "No path exists":
        print(result)
        return []
    else:
        print(f"Minimum cost: {result}")
        path_str = " → ".join(map(str, path))
        print(f"Path: {path_str}")
        return path

if __name__ == "__main__":
    main()