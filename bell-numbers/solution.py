class BellNumbers:
    def __init__(self, max_n):
        self.max_n = max_n
        self.bell_cache = {}
    
    def compute_bell(self, mod):
        """Compute Bell numbers up to max_n modulo mod"""
        if mod in self.bell_cache:
            return self.bell_cache[mod]
        
        bell = [0] * (self.max_n + 1)
        bell[0] = 1
        
        # Precompute binomial coefficients
        C = [[0] * (self.max_n + 1) for _ in range(self.max_n + 1)]
        for i in range(self.max_n + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % mod
        
        # Compute Bell numbers using recurrence
        for i in range(1, self.max_n + 1):
            for j in range(i):
                bell[i] = (bell[i] + C[i-1][j] * bell[j]) % mod
        
        self.bell_cache[mod] = bell
        return bell
    
    def get_bell(self, n, mod):
        """Get B(n) % mod"""
        if n > self.max_n:
            self.max_n = n
            self.bell_cache.clear()
        
        if mod not in self.bell_cache:
            self.compute_bell(mod)
        
        return self.bell_cache[mod][n]

def solve_bell_numbers():
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
        temp_idx += 2
    
    bell_calculator = BellNumbers(max_n)
    
    for _ in range(t):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2
        
        result = bell_calculator.get_bell(n, m)
        results.append(str(result))
    
    return results