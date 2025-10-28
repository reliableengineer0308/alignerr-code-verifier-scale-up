def solve(data):
    # Parse input data
    idx = 0
    M = data[idx]; idx += 1
    N = data[idx]; idx += 1
    K = data[idx]; idx += 1
    
    # Read grid
    grid = []
    for i in range(M):
        row = []
        for j in range(N):
            row.append(data[idx]); idx += 1
        grid.append(row)
    
    # DP state: dp[i][j][dir][k] = max gold at (i,j) coming from direction 'dir' with k consecutive moves
    # dir: 0=right, 1=down
    INF = -10**9
    dp = [[[[INF] * (K + 1) for _ in range(2)] for _ in range(N)] for _ in range(M)]
    
    # Initialize starting position (no previous direction)
    dp[0][0][0][0] = grid[0][0]
    dp[0][0][1][0] = grid[0][0]
    
    for i in range(M):
        for j in range(N):
            for prev_dir in range(2):  # 0=right, 1=down
                for consec in range(K + 1):
                    if dp[i][j][prev_dir][consec] == INF:
                        continue
                    
                    current_gold = dp[i][j][prev_dir][consec]
                    
                    # Move right
                    if j + 1 < N:
                        if prev_dir == 0:  # Previous move was also right
                            new_consec = consec + 1
                        else:  # Changing direction
                            new_consec = 1
                        
                        if new_consec <= K:
                            new_gold = current_gold + grid[i][j + 1]
                            if new_gold > dp[i][j + 1][0][new_consec]:
                                dp[i][j + 1][0][new_consec] = new_gold
                    
                    # Move down
                    if i + 1 < M:
                        if prev_dir == 1:  # Previous move was also down
                            new_consec = consec + 1
                        else:  # Changing direction
                            new_consec = 1
                        
                        if new_consec <= K:
                            new_gold = current_gold + grid[i + 1][j]
                            if new_gold > dp[i + 1][j][1][new_consec]:
                                dp[i + 1][j][1][new_consec] = new_gold
    
    # Find maximum at destination
    result = INF
    for dir in range(2):
        for consec in range(K + 1):
            result = max(result, dp[M - 1][N - 1][dir][consec])
    
    return result if result != INF else -1