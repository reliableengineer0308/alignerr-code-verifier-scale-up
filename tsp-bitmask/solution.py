import sys

def solve_tsp(dist):
    """Solve TSP using DP with bitmask"""
    n = len(dist)
    if n == 1:
        return 0
    
    # dp[mask][i] = minimum cost to visit all cities in mask ending at city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    
    # Initialize: starting from city 0
    # After visiting only city i (from city 0), the cost is dist[0][i]
    for i in range(1, n):
        dp[1 << i][i] = dist[0][i]
    
    # Also include the case where we start at city 0 (mask with only city 0)
    # This is the base case: we're at city 0, having visited only city 0
    dp[1][0] = 0  # mask=1 (only city 0 visited), at city 0, cost=0
    
    # Iterate over all masks
    for mask in range(1 << n):
        for i in range(n):
            # If city i is not in the current mask, skip
            if not (mask & (1 << i)):
                continue
            
            # If this state is not reached yet, skip
            if dp[mask][i] == float('inf'):
                continue
            
            # Try to extend to unvisited cities
            for j in range(n):
                # If city j is already visited, skip
                if mask & (1 << j):
                    continue
                
                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + dist[i][j]
                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
    
    # Find the minimum cost to visit all cities and return to start
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    for i in range(n):
        if dp[full_mask][i] != float('inf'):
            # Return to starting city 0
            min_cost = min(min_cost, dp[full_mask][i] + dist[i][0])
    
    return min_cost if min_cost != float('inf') else 0

def solve_tsp_cases():
    """Main function to handle multiple test cases"""
    data = sys.stdin.read().split()
    if not data:
        return []
    
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        dist = []
        for i in range(n):
            row = list(map(int, data[idx:idx+n]))
            idx += n
            dist.append(row)
        
        result = solve_tsp(dist)
        results.append(str(result))
    
    return results