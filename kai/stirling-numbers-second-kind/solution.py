class StirlingNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.stirling_cache = {}
    
    def compute_stirling(self, mod):
        """Compute Stirling numbers up to max_n modulo mod"""
        if mod in self.stirling_cache:
            return self.stirling_cache[mod]
        
        # Initialize DP table
        dp = [[0] * (self.max_n + 1) for _ in range(self.max_n + 1)]
        dp[0][0] = 1
        
        for i in range(1, self.max_n + 1):
            for j in range(1, i + 1):
                dp[i][j] = (j * dp[i-1][j] + dp[i-1][j-1]) % mod
        
        self.stirling_cache[mod] = dp
        return dp
    
    def get_stirling(self, n, k, mod):
        """Get S(n, k) % mod"""
        if n < k:
            return 0
        if n > self.max_n:
            # Extend if needed
            self.max_n = n
            self.stirling_cache.clear()
        
        if mod not in self.stirling_cache:
            self.compute_stirling(mod)
        
        return self.stirling_cache[mod][n][k]

def solve_stirling_numbers():
    import sys
    input = sys.stdin.read().split()
    
    t = int(input[0])
    idx = 1
    results = []
    
    # Find maximum n for precomputation
    max_n = 0
    temp_idx = idx
    for _ in range(t):
        n = int(input[temp_idx])
        max_n = max(max_n, n)
        temp_idx += 3
    
    stirling_calculator = StirlingNumbers(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        k = int(input[idx + 1])
        m = int(input[idx + 2])
        idx += 3
        
        result = stirling_calculator.get_stirling(n, k, m)
        results.append(str(result))
    
    return results