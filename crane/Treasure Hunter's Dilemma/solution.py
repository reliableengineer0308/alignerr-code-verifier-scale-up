def solve(data):
    n = data[0]
    chambers = data[1:1+n]
    
    if n == 0:
        return 0
    if n == 1:
        return chambers[0]
    
    # DP array: dp[i] represents maximum gold that can be collected up to chamber i
    dp = [0] * n
    dp[0] = chambers[0]
    dp[1] = max(chambers[0], chambers[1])
    
    for i in range(2, n):
        # Either take current chamber + dp[i-2], or skip current and take dp[i-1]
        dp[i] = max(dp[i-1], dp[i-2] + chambers[i])
        
    return dp[n-1]